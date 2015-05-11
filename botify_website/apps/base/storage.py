import urlparse

from django.contrib.staticfiles.storage import CachedFilesMixin
from django.conf import settings

from storages.backends.s3boto import S3BotoStorage
from pipeline.storage import PipelineMixin


def domain(url):
        return urlparse.urlparse(url).hostname


class CachedS3BotoStorage(CachedFilesMixin, S3BotoStorage):
    pass


class StaticFilesStorage(CachedS3BotoStorage):
    def __init__(self, *args, **kwargs):
        kwargs['bucket'] = settings.AWS_STORAGE_BUCKET_NAME
        kwargs['custom_domain'] = domain(settings.STATIC_URL)
        super(StaticFilesStorage, self).__init__(*args, **kwargs)


class S3PipelineStorage(PipelineMixin, CachedFilesMixin, S3BotoStorage):

    def __init__(self, *args, **kwargs):
        kwargs['bucket'] = settings.AWS_STORAGE_BUCKET_NAME
        kwargs['custom_domain'] = domain(settings.STATIC_URL)
        if settings.STATIC_URL.startswith('https'):
            kwargs['secure_urls'] = True
        super(S3PipelineStorage, self).__init__(*args, **kwargs)
