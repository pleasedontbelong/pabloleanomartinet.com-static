from django.conf.urls import include, url


urlpatterns = [
    url(r'^', include('default_theme.urls')),
    url(r'^', include('blog.urls')),
]
