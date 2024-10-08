from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5+f#!xn=hj^u#=cr9@pz@@5cf7bqf0ymy=8uyfpx_zvxpght3='

ADMINS = (
    ('Michael Yin', 'admin@michaelyin.info'),
)

STATIC_ROOT = "/staticfiles"
MEDIA_ROOT = "/mediafiles"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass
