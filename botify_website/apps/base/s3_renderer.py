# -*- coding: utf-8 -*-
import cStringIO

from datetime import timedelta, datetime
from django.conf import settings
from django.test.client import Client
from django_medusa.renderers.base import BaseStaticSiteRenderer

from boto.s3.connection import S3Connection

__all__ = ('S3StaticSiteRenderer', )


class BucketCache(object):
    BUCKET_CACHE = {}
    CONN = None

    @classmethod
    def s3_conn(cls):
        if not cls.CONN:
            cls.CONN = S3Connection()
        return cls.CONN

    @classmethod
    def _get_bucket(cls, bucket=None):
        if bucket in cls.BUCKET_CACHE:
            return cls.BUCKET_CACHE[bucket]
        if not bucket:
            bucket = settings.AWS_WEBSITE_BUCKET_NAME
        cls.BUCKET_CACHE[bucket] = cls.s3_conn().get_bucket(bucket)
        cls.BUCKET_CACHE[bucket].configure_website("index.html", "500.html")
        return cls.BUCKET_CACHE[bucket]


def _get_cf():
    from boto.cloudfront import CloudFrontConnection
    return CloudFrontConnection(
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )


def _get_distribution():
    if not getattr(settings, "AWS_DISTRIBUTION_ID", None):
        return None

    conn = _get_cf()
    try:
        return conn.get_distribution_info(settings.AWS_DISTRIBUTION_ID)
    except:
        return None


def _upload_to_s3(key, file, response, metadata=None):
    cache_time = getattr(settings, 'MEDUSA_S3_MAX_AGE', 0)
    now = datetime.now()
    expire_dt = now + timedelta(seconds=cache_time)
    if cache_time is not None:
        key.set_metadata(
            'Cache-Control',
            'max-age=%d, must-revalidate' % int(cache_time)
        )
        key.set_metadata(
            'Expires',
            expire_dt.strftime("%a, %d %b %Y %H:%M:%S GMT")
        )
        if metadata:
            for k, v in metadata.iteritems():
                key.set_metadata(k, v)
    if response.status_code in (301, 302):
        key.set_redirect(response['location'].replace('http://testserver', ''))

    else:
        key.set_contents_from_file(file, policy="public-read")
    key.make_public()


def _s3_render_path(args):
    client, conf, view = args
    path = conf["path"]
    if not client:
        client = Client()

    if "bucket" in conf:
        bucket = BucketCache._get_bucket(conf["bucket"])
    else:
        bucket = BucketCache._get_bucket()
    resp = client.get(path)

    if resp.status_code not in (200, 301, 302):
        raise Exception('path {} has returned a {} code'.format(path, resp.status_code))

    # Default to "index.html" as the upload path if we're in a dir listing.
    outpath = path
    if path.endswith("/"):
        outpath += "index.html"
    if outpath.startswith('/'):
        outpath = outpath[1:]

    key = bucket.get_key(outpath) or bucket.new_key(outpath)
    key.content_type = resp['Content-Type']

    temp_file = cStringIO.StringIO(resp.content)
    md5 = key.compute_md5(temp_file)

    # If key is new, there's no etag yet
    if not key.etag:
        _upload_to_s3(key, temp_file, resp, conf.get("metadata"))
        message = "Creating"

    else:
        etag = key.etag or ''
        # for some weird reason, etags are quoted, strip them
        etag = etag.strip('"').strip("'")
        if etag not in md5:
            _upload_to_s3(key, temp_file, resp, conf.get("metadata"))
            message = "Updating"
        else:
            message = "Skipping"

    print "%s %s %s" % (
        message,
        bucket.get_website_endpoint(),
        outpath
    )
    temp_file.close()
    return [path, outpath]


class S3StaticSiteRenderer(BaseStaticSiteRenderer):
    """
    A variation of BaseStaticSiteRenderer that deploys directly to S3
    rather than to the local filesystem.
    Requires `boto`.
    Uses some of the same settings as `django-storages`:
      * AWS_ACCESS_KEY
      * AWS_SECRET_ACCESS_KEY
      * AWS_STORAGE_BUCKET_NAME
    """
    @classmethod
    def initialize_output(cls):
        cls.all_generated_paths = []

    @property
    def s3_conn(self):
        if not hasattr(self, '_s3_conn'):
            self._s3_conn = S3Connection(
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                is_secure=False
            )
        return self._s3_conn

    def generate(self):
        self.generated_paths = []
        if getattr(settings, "MEDUSA_MULTITHREAD", False):
            # Upload up to ten items at once via `multiprocessing`.
            from multiprocessing import Pool
            import itertools

            print "Uploading with up to 10 upload processes..."
            pool = Pool()
            path_tuples = pool.map(
                _s3_render_path,
                ((None, path, None) for path in self.paths),
                chunksize=5
            )
            pool.close()
            pool.join()
            self.generated_paths = list(itertools.chain(*path_tuples))
        else:
            # Use standard, serial upload.
            self.client = Client()
            for path in self.paths:
                self.generated_paths += _s3_render_path((self.client, path, None))

        type(self).all_generated_paths += self.generated_paths

    @classmethod
    def finalize_output(cls):
        pass
