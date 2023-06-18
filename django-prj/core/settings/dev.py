from . base import *

# DEBUG is set in .env file:
# DEBUG = True

INSTALLED_APPS += [
    "django_extensions",
]

# media_root is needed only in dev as in prod we are using cloudinary
MEDIA_ROOT = BASE_DIR / 'MEDIA_ROOT'

# we need static_root only in prod, but can set it in dev also to make some tests...
STATIC_ROOT = BASE_DIR / 'STATIC_ROOT'
