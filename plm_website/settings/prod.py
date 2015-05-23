from .base import *

DEBUG = False

AWS_STORAGE_BUCKET_NAME = 'xxxxxxxxxxxxxxxxxxxxxx'
AWS_WEBSITE_BUCKET_NAME = 'xxxxxxxxxxxxxxxxxxxxxx'
AWS_S3_SECURE_URLS = False
AWS_QUERYSTRING_AUTH = False
STATICFILES_STORAGE = 'base.storage.S3PipelineStorage'

ALLOWED_HOSTS = ['*']

STATIC_URL = 'https://static.botify.com/'
