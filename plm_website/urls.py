from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^', include('default_theme.urls')),
    url(r'^', include('blog.urls')),
)
