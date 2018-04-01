from django.conf.urls import url
from plm_website.core.generic import TemplateView


urlpatterns = [
    url(r'^$',
        TemplateView.as_view(template_name='pages/homepage.jinja2'),
        name='homepage'),
    url(r'^posts/?$',
        TemplateView.as_view(template_name='pages/posts.jinja2'),
        name='posts-list'),
    url(r'^projects/?$',
        TemplateView.as_view(template_name='pages/projects.jinja2'),
        name='projects-list'),
    url(r'^about-me/?$',
        TemplateView.as_view(template_name='pages/about_me.jinja2'),
        name='about-me')
]
