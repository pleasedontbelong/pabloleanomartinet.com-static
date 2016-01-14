# -*- coding: utf-8 -*-
import os
from .base import *

ALLOWED_HOSTS = [os.getenv('VIRTUAL_HOST', 'localhost')]
DEBUG = False
TEMPLATE_DEBUG = False
