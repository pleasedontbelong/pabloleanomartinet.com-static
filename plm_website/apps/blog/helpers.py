# -*- coding: utf-8 -*-
from .utils import list_posts, list_projects


def posts_list(limit=None):
    return list_posts(limit)


def projects_list(limit=None):
    return list_projects(limit)
