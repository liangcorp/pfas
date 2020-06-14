# In production set the environment variable like this:
#    DJANGO_SETTINGS_MODULE=web_personal_finance.settings.production
from .base import *  # NOQA

# For security and performance reasons, DEBUG is turned off
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['mysite.com', ]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

EMAIL_HOST = "localhost"
EMAIL_HOST_PASSWORD = ""
EMAIL_HOST_USER = ""
EMAIL_PORT = ""
EMAIL_SUBJECT_PREFIX = ""
EMAIL_USE_TLS = True


# Must mention ALLOWED_HOSTS in production!
# ALLOWED_HOSTS = ["web_personal_finance.com"]

# Cache the templates in memory for speed-up
loaders = [
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]

TEMPLATES[0]["OPTIONS"].update({"loaders": loaders})
TEMPLATES[0].update({"APP_DIRS": False})

# Define STATIC_ROOT for the collectstatic command
STATIC_ROOT = BASE_DIR + "/site" + "/static"
