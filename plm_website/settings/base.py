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
from django_jinja.builtins import DEFAULT_EXTENSIONS

ROOT = realpath(join(dirname(__file__), '..'))
BASE_DIR = realpath(join(ROOT, '..'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wd=7)0b+rurkk@m1qnase3w1p2%urw%-__4o3=i)f$hh4it=&@s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    {
        "NAME": "jinja2",
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".jinja2",
            "app_dirname": "jinja2",
            "auto_reload": True,  # Set to False in prod
            "extensions": DEFAULT_EXTENSIONS + ["pipeline.jinja2.PipelineExtension"],
            "globals": {
                "posts_list": "plm_website.apps.blog.helpers.posts_list",
                "projects_list": "plm_website.apps.blog.helpers.projects_list"
            },
        }
    },
]


ALLOWED_HOSTS = ['localhost']

path[0:0] = [
    join(ROOT, 'apps'),
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'plm_website.core',
    'content',
    'blog',
    'default_theme',
    'django_extensions',
    'pipeline'
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'plm_website.urls'

WSGI_APPLICATION = 'plm_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'plmstatic.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'TEST': {
            'NAME': 'plmstatic_test.db',
        },
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
STATIC_ROOT = join(ROOT, '..', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = join(ROOT, '..', 'media')

MEDUSA_RENDERER_CLASS = "base.s3_renderer.S3StaticSiteRenderer"
MEDUSA_MULTITHREAD = False
MEDUSA_UPDATE_ASYNC = True
MEDUSA_S3_MAX_AGE = 10


# PIPELINE CONFIGURATION

STATICFILES_STORAGE = "pipeline.storage.PipelineCachedStorage"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "pipeline.finders.PipelineFinder",
)

PIPELINE = {
    "JAVASCRIPT": {
        "main": {
            "source_filenames": (
                'vendors/jquery/dist/jquery.min.js',
                'vendors/bootstrap/dist/js/bootstrap.min.js',
                'vendors/highlightjs/highlight.pack.js',
            ),
            "output_filename": "js/script.js",
        }
    },
    'STYLESHEETS': {
        'main': {
            'source_filenames': (
                'vendors/bootstrap/dist/css/bootstrap.min.css',
                'css/main.css',
                'vendors/highlightjs/styles/github.css',
            ),
            'output_filename': 'css/main.css',
            'extra_context': {
                'media': 'screen',
            },
        },
        'main_print': {
            'source_filenames': (
                'bootstrap/dist/css/bootstrap.min.css',
                'css/print.css',
            ),
            'output_filename': 'css/main.print.css',
            'extra_context': {
                'media': 'print',
            },
        },
    },
    'CSS_COMPRESSOR': None,
    'JS_COMPRESSOR': None,
    'MIMETYPES': (
        ('text/coffeescript', '.coffee'),
        ('text/less', '.less'),
        ('text/javascript', '.js'),
        ('text/x-sass', '.sass'),
        ('text/x-scss', '.scss')
    ),
}


# needed for django suit
# from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
# TEMPLATE_CONTEXT_PROCESSORS = TCP + (
#     'django.core.context_processors.request',
# )

POST_TEMPLATES_APP = "plm_website.apps.content.jinja2.posts.{}_meta"
POSTS_PATH = "content/jinja2/posts"
POST_EXTENSIONS = ('_meta.py', '_meta.pyc', '_meta.pyo')
