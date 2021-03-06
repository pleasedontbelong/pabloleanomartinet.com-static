# -*- coding: utf-8 -*-
import imp
import os

from django.conf import settings

from .models import Post


class PostManager(object):
    """
    Class that manages the posts list
    """
    def __init__(self):
        self.posts = []
        self.index = 0

    def __iter__(self):
        return self

    def __getitem__(self, key):
        return self.posts[key]

    def next(self):
        if self.index >= len(self.posts):
            raise StopIteration
        else:
            next = self.posts[self.index]
            self.index += 1
            return next

    def all(self):
        file, pathname, description = imp.find_module(settings.POSTS_PATH)
        if file:
            raise ImportError('Not a package: %r', settings.POSTS_PATH)

        posts_files = set()
        for module in os.listdir(pathname):
            if module.endswith(settings.POST_EXTENSIONS):
                posts_files.add(os.path.splitext(module)[0][:-5])

        self.posts = []
        for post_file in posts_files:
            post = Post(post_file)
            post.load_data()
            self.posts.append(post)
        return self

    def filter(self, **filters):
        self.all()
        self.posts = [p for p in self.posts if p.match(filters)]
        return self

    def order_by(self, attribute, reverse=True):
        self.posts.sort(key=lambda p: getattr(p.data, attribute), reverse=reverse)
        return self

    def get(self, **filters):
        results = self.filter(**filters)
        if not results:
            return None
        return results[0]
