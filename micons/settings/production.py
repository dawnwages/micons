from __future__ import absolute_import, unicode_literals

from .base import *
import dj_database_url

DEBUG = False

ENVIRONMENT = 'production'

ALLOWED_HOSTS = ['']

DATABASES['default'] = dj_database_url.config(
    default='postgres://postgres@localhost:5432/micons_db'
)

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
        'INDEX': 'micons'
    }
}


CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'KEY_PREFIX': 'micons',
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
        }
    }
}

# Use the cached template loader
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

try:
    from .local import *
except ImportError:
    pass
