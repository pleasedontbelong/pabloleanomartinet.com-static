from datetime import datetime
from .constants import CATEGORIES

CATEGORY = CATEGORIES.POST
AUTHOR = "Pablo"
POST_TITLE = "Databaseless blog in django. Built from scratch"
POST_DESCRIPTION = "Why I decided to create a blog from scratch wihout a database" \
                   " and using django framework in order to keep my posts under" \
                   " versioning and throw away wordpress forever"
POST_TAGS = ("django", "wordpress", "blog", "databaseless")
PUBLISHED_DATE = datetime(year=2015, month=7, day=13)
