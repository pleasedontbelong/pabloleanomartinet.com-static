from django.conf.urls import patterns, url
from .views import PostView


urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[\w\-]+)/?$',
        PostView.as_view(),
        name='post_view')
)
