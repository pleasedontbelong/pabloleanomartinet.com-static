# -*- coding: utf-8 -*-
import os
from .base import *

ALLOWED_HOSTS = [os.getenv('VIRTUAL_HOST', 'localhost')]
DEBUG = False
TEMPLATE_DEBUG = False

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
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',  # Not recommended.
        }
    },
}


STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
