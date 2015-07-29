from datetime import datetime
from .constants import CATEGORIES

CATEGORY = CATEGORIES.PROJECT
AUTHOR = "Pablo"
POST_TITLE = "The before and after of rebuilding my blog in python"
POST_DESCRIPTION = "After finishing my new blog, I try to compare my old" \
                   "blog (wordpress) and my new blog (django site), using" \
                   "Botify"

POST_TAGS = ("django", "wordpress", "blog", "botify")
PUBLISHED_DATE = datetime(year=2015, month=7, day=23)
