"""
Django settings for plm_website project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import dirname, join, realpath
from sys import path

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
    'plm_website.core',
    'content',
    'blog',
    'default_theme',
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

ROOT_URLCONF = 'plm_website.urls'

WSGI_APPLICATION = 'plm_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'plm_static',
        'USER': 'django_test',
        'PASSWORD': '$ecret',
        'HOST': 'localhost',
        'PORT': '5432'
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
    'default': {
        'source_filenames': (
            'vendors/bootstrap/dist/css/bootstrap.min.css',
            'css/main.css',
        ),
        'output_filename': 'css/main.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'default': {
        'source_filenames': (
            'vendors/jquery/dist/jquery.min.js',
            'vendors/bootstrap/dist/js/bootstrap.min.js'
        ),
        'output_filename': 'js/script.js',
    }
}


# needed for django suit
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

POST_TEMPLATES_APP = "plm_website.apps.content.templates.posts.{}_meta"
POSTS_PATH = "content/templates/posts"
POST_EXTENSIONS = ('_meta.py', '_meta.pyc', '_meta.pyo')
