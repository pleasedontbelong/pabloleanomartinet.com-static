"""
Django settings for botify_website project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import dirname, join, realpath
from sys import path
import os

ROOT = realpath(join(dirname(__file__), '..'))
BASE_DIR = realpath(join(ROOT, '..'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wd=7)0b+rurkk@m1qnase3w1p2%urw%-__4o3=i)f$hh4it=&@s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

TEMPLATE_LOADERS = (
    'jingo.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

ALLOWED_HOSTS = ['localhost']

path[0:0] = [
    join(ROOT, 'apps'),
]

# Application definition

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'django_medusa',
    'base',
    'website',
    'storages',
    'django_extensions',
    'pipeline'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'botify_website.urls'

WSGI_APPLICATION = 'botify_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = join(BASE_DIR, 'static')

JINGO_INCLUDE_PATTERN = r'^.*(website/.+\.html|pure_pagination/.+\.html|\.jinja2)$'

JINJA_CONFIG = {
    'autoescape': False,
    'extensions': [
        'jinja2.ext.i18n',
        'jinja2.ext.with_',
        'pipeline.jinja2.ext.PipelineExtension'
    ]
}


MEDUSA_RENDERER_CLASS = "base.s3_renderer.S3StaticSiteRenderer"
MEDUSA_MULTITHREAD = False
MEDUSA_UPDATE_ASYNC = True
MEDUSA_S3_MAX_AGE = 10


FASTLY_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXX'


# PIPELINE CONFIGURATION

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE_YUGLIFY_BINARY = "node_modules/yuglify/bin/yuglify"
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'

PIPELINE_CSS = {
    'main': {
        'source_filenames': (
            'plugins/bootstrap/css/bootstrap.min.css',
            'plugins/font-awesome/css/font-awesome.css',
            'plugins/flexslider/flexslider.css',
            'plugins/rrssb/css/rrssb.css',
            'css/botify.css',
            'css/ios7-fix.css'
        ),
        'output_filename': 'css/style.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'main': {
        'source_filenames': (
            'plugins/jquery-1.11.1.min.js',
            'plugins/jquery-migrate-1.2.1.min.js',
            'plugins/bootstrap/js/bootstrap.min.js',
            'plugins/bootstrap-hover-dropdown.min.js',
            'plugins/back-to-top.js',
            'plugins/jquery-placeholder/jquery.placeholder.js',
            'plugins/FitVids/jquery.fitvids.js',
            'plugins/flexslider/jquery.flexslider-min.js',
            'plugins/rrssb/js/rrssb.min.js',
            'js/main.js',
            'js/jquery.stickytableheaders.min.js'
        ),
        'output_filename': 'js/script.js',
    }
}


#needed for django suit
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

REDIRECTS = (
    ('tour/', '/features/'),
    ('fonctionnalites-botify/', '/features/'),
    ('analytics/', '/'),
    ('cgv/', '/terms-privacy/'),
    ('seo-log-analyzer/', '/log-analyzer/'),
    ('agences/', '/partners/'),
    ('pricing/pay-as-you-go.html', '/pricing/')
)
