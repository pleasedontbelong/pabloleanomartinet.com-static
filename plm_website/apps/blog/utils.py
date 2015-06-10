# -*- coding: utf-8 -*-
import imp
import os
MODULE_EXTENSIONS = ('.py', '.pyc', '.pyo')
POSTS_PATH = "blog/templates/posts"


def package_contents(package_name):
    file, pathname, description = imp.find_module(package_name)
    if file:
        raise ImportError('Not a package: %r', package_name)
    # Use a set because some may be both source and compiled.
    return set([os.path.splitext(module)[0] for module in os.listdir(pathname) if module.endswith(MODULE_EXTENSIONS)])


def list_posts():
    """
    :return : list
    parses the posts templates and return a list of post identifiers
    """
