from django.contrib.staticfiles.storage import staticfiles_storage
from django.template import Context, defaultfilters
from django.conf import settings

from jinja2 import contextfunction
from jingo import register


@register.function
def static(path):
    return staticfiles_storage.url(path)
