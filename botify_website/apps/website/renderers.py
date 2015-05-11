from django_medusa.renderers import StaticSiteRenderer

from django.conf import settings
from .utils import get_html_pages_from_site


class BotifyWebsiteRenderer(StaticSiteRenderer):
    def get_paths(self):
        paths = []

        for page in [src for src, _ in settings.REDIRECTS] + get_html_pages_from_site():
            paths.append({
                "path": "/{}".format(page),
                "bucket": settings.AWS_WEBSITE_BUCKET_NAME
            })
        return paths

renderers = [BotifyWebsiteRenderer,]

