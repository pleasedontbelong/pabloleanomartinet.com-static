# -*- coding: utf-8 -*-
from jingo import register
from .utils import list_posts, list_projects


@register.function
def posts_list(limit=None):
    return list_posts(limit)


@register.function
def projects_list(limit=None):
    return list_projects(limit)
