from datetime import datetime
from .constants import CATEGORIES

CATEGORY = CATEGORIES.POST
AUTHOR = "Pablo"
POST_TITLE = "Setting Django with Jinja2 and Babel for i18n"
POST_DESCRIPTION = "How to configure django to be able to extract the" \
                   " translation messages with jinja2 using babel."

POST_TAGS = ("django", "jinja2", "babel", "i18n", "gettext")

PUBLISHED_DATE = datetime(year=2018, month=4, day=1)
