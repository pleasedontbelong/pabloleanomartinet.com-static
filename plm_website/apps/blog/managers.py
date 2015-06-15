# -*- coding: utf-8 -*-
import imp
import os
POST_EXTENSIONS = ('_meta.py', '_meta.pyc', '_meta.pyo')
POSTS_PATH = "blog/templates/posts"


class PostManager(object):
    """
    Class that manages the posts list
    """
    def __init__(self):
        self.posts_list = list(self._find_posts())

    def _find_posts(self):
        posts_list = set()
        file, pathname, description = imp.find_module(POSTS_PATH)
        if file:
            raise ImportError('Not a package: %r', POSTS_PATH)

        for module in os.listdir(pathname):
            if module.endswith(POST_EXTENSIONS):
                posts_list.add(os.path.splitext(module)[0][:-5])
        return posts_list
