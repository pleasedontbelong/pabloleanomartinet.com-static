import os
from .base import *  # NOQA


ALLOWED_HOSTS = [os.getenv('VIRTUAL_HOST', 'localhost')]
DEBUG = True
TEMPLATE_DEBUG = True
