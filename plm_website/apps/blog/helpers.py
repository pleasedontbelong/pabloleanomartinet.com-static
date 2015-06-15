# -*- coding: utf-8 -*-
from jingo import register
from .utils import list_posts


@register.function
def posts_list():
    return list_posts()
