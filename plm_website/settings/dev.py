from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

AWS_STORAGE_BUCKET_NAME = 'xxxxxxxxxxxxxxxxxxx'
AWS_WEBSITE_BUCKET_NAME = 'xxxxxxxxxxxxxxxxxxx'
AWS_S3_SECURE_URLS = False
AWS_QUERYSTRING_AUTH = False
STATICFILES_STORAGE = 'base.storage.S3PipelineStorage'

ALLOWED_HOSTS = ['*']

STATIC_URL = 'https://static-dev.botify.com/'

STATIC_WEBSITE_BUCKET = 'com.botify.saas.dev.website'
