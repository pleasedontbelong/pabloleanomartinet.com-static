# -*- coding: utf-8 -*-
from plm_website.core.generic import TemplateView
from .models import Post


class PostView(TemplateView):

    def get(self, *args, **kwargs):
        self.post_slug = kwargs.get('slug')
        return super(PostView, self).get(*args, **kwargs)

    def get_template_names(self):
        return "posts/{}.jinja2".format(self.post_slug)

    def get_context_data(self, *args, **kwargs):
        post = Post(self.post_slug)
        post.load_data()
        return dict(
            super(PostView, self).get_context_data(*args, **kwargs),
            **{
                'post': post
            }
        )
