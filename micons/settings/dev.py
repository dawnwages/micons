from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

BASE_URL = 'http://localhost:8000'

try:
    from .local import *
except ImportError:
    pass
