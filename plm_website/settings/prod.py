# -*- coding: utf-8 -*-
import os
from .base import *

ALLOWED_HOSTS = [os.getenv('VIRTUAL_HOST', 'localhost')]
DEBUG = True
TEMPLATE_DEBUG = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',  # Not recommended.
        }
    },
}
