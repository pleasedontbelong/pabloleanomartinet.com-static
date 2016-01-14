import os

APP_ENVIRONMENT = os.getenv('APP_ENVIRONMENT')

if APP_ENVIRONMENT == "production":
    from .prod import *
else:
    from .local import *
