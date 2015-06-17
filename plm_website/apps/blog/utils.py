# -*- coding: utf-8 -*-
from .managers import PostManager


def list_posts():
    """
    :return : list
    parses the posts templates and return a list of post identifiers
    """
    manager = PostManager()
    return manager.all()
