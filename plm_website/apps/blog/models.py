# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse
from importlib import import_module


class Post(object):
    def __init__(self, slug):
        self.slug = slug
        self.data = None

    def load_data(self):
        self.data = import_module(settings.POST_TEMPLATES_APP.format(self.slug))

    @property
    def link(self):
        return reverse('post_view', kwargs={'slug': self.slug})
