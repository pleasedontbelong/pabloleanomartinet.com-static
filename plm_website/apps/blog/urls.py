from django.conf.urls import url
from .views import PostView


urlpatterns = [
    url(r'^(?P<slug>[\w\-]+)/$',
        PostView.as_view(),
        name='post_view')
]
