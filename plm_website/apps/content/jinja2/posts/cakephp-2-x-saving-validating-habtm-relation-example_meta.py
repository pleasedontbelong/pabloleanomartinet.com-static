from datetime import datetime
from .constants import CATEGORIES

CATEGORY = CATEGORIES.POST
AUTHOR = "Pablo"
POST_TITLE = "CakePHP 2.x Saving and validating a HABTM relation example"
POST_DESCRIPTION = "A basic example of saving a HABTM relationship in cakephp 2.x," \
                   " while also validating (server-side) the number of items saved"
POST_TAGS = ("CakePHP", "HAMTB", "save", "example")
PUBLISHED_DATE = datetime(year=2014, month=1, day=24)
