# -*- coding: utf-8 -*-
from .managers import PostManager
from content.jinja2.posts.constants import CATEGORIES


def list_posts(limit=None):
    """
    :return : list
    parses the posts templates and return a list of post
    """
    return _list(limit, CATEGORIES.POST)


def list_projects(limit=None):
    """
    :return : list
    parses the posts templates and return a list of post with the category "Project"
    """
    return _list(limit, CATEGORIES.PROJECT)


def _list(limit, category):
    manager = PostManager()
    posts = manager.filter(CATEGORY=category).order_by('PUBLISHED_DATE')
    if limit:
        return posts[:limit]
    return posts
