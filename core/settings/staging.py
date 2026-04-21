from .base import *

DEBUG = False
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASES = {
    'default': env.db('DATABASE_URL')
}

# Static files served by Nginx
STATIC_ROOT = BASE_DIR / 'staticfiles'
