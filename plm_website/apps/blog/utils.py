# -*- coding: utf-8 -*-
from .managers import PostManager
from blog.templates.posts.constants import CATEGORIES


def list_posts(limit=None):
    """
    :return : list
    parses the posts templates and return a list of post identifiers
    """
    manager = PostManager()
    posts = manager.filter(CATEGORY=CATEGORIES.POST).order_by('PUBLISHED_DATE')
    # posts = manager.all().order_by('PUBLISHED_DATE')
    if limit:
        return posts[:limit]
    return posts
