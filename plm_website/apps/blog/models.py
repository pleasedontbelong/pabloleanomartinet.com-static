# -*- coding: utf-8 -*-
from django.http import Http404
from django.conf import settings
from django.core.urlresolvers import reverse
from importlib import import_module


class Post(object):
    def __init__(self, slug):
        self.slug = slug
        self.data = None

    def load_data(self):
        try:
            self.data = import_module(settings.POST_TEMPLATES_APP.format(self.slug))
        except ImportError:
            raise Http404("Page or Post not found")


    @property
    def url(self):
        return reverse('post_view', kwargs={'slug': self.slug})

    def match(self, filters):
        for filter_name, filter_value in filters.iteritems():
            if getattr(self.data, filter_name) != filter_value:
                return False
        return True
