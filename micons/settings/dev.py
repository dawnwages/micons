from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+51mvjypkj(6pt^d$2+e_rry(3^yh5k0fqj42gmcvxw)9_^rzo'
#mysecret = '+2p^yh!0gj*7bd0k6xrr9x)tab+fyp#4eu9tf!6kefcp*n&22$'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
