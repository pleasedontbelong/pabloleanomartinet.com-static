from django.conf import settings
from importlib import import_module
from plm_website.core.generic import TemplateView


class PostView(TemplateView):

    def get(self, *args, **kwargs):
        self.post_slug = kwargs.get('slug')
        return super(PostView, self).get(*args, **kwargs)

    def get_template_names(self):
        return "posts/{}.jinja2".format(self.post_slug)

    def get_context_data(self, *args, **kwargs):
        meta = import_module(settings.POST_TEMPLATES_APP.format(self.post_slug))
        return dict(
            super(PostView, self).get_context_data(*args, **kwargs),
            **{
                'meta': meta
            }
        )
