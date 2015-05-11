from django.conf.urls import patterns, url
from django.conf import settings
from django.views.generic import RedirectView

from .views import PageView

# Redirect views
urlpatterns = patterns('', *[url(r'^{}(\/?)$'.format(src), RedirectView.as_view(url=dst, permanent=True)) for src, dst in settings.REDIRECTS])

# Static files views
urlpatterns += patterns('',
    url(r'^$', PageView.as_view(), name="website_page"),
    url(r'^(?P<path>.+)$', PageView.as_view(), name="website_page"),
)
