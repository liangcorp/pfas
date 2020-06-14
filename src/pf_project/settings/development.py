from .base import *  # NOQA


INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}

EMAIL_HOST = "192.168.1.6"
EMAIL_PORT = "1025"
EMAIL_SUBJECT_PREFIX = "NOREPLY"
