# -*- coding: utf-8 -*-
import imp
import os
POST_EXTENSIONS = ('_meta.py', '_meta.pyc', '_meta.pyo')
POSTS_PATH = "blog/templates/posts"

from .models import Post


class PostManager(object):
    """
    Class that manages the posts list
    """

    def all(self):

        file, pathname, description = imp.find_module(POSTS_PATH)
        if file:
            raise ImportError('Not a package: %r', POSTS_PATH)

        posts_files = set()
        for module in os.listdir(pathname):
            if module.endswith(POST_EXTENSIONS):
                posts_files.add(os.path.splitext(module)[0][:-5])

        posts = []
        for post_file in posts_files:
            post = Post(post_file)
            post.load_data()
            posts.append(post)
        return posts
