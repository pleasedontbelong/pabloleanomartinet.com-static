"""
WSGI config for gettingstarted project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
from newrelic import agent
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "plm_website.settings")

application = get_wsgi_application()
application = agent.WSGIApplicationWrapper(application)
