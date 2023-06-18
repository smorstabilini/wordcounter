from .base import *

# read it from .env!
# DEBUG = False

STATIC_ROOT = BASE_DIR / 'STATIC_ROOT'

# to use WhiteNoise to serve static files in production:
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# adding Whitenoise middleware just after SecurityMiddleware:
whitenoise_middleware_position = MIDDLEWARE.index('django.middleware.security.SecurityMiddleware') + 1
MIDDLEWARE.insert(whitenoise_middleware_position, 'whitenoise.middleware.WhiteNoiseMiddleware')
