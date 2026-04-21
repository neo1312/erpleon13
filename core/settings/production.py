from .base import *

DEBUG = False
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASES = {
    'default': env.db('DATABASE_URL')
}

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SESSION_COOKIE_SECURE = False  # Set True when HTTPS is enabled
CSRF_COOKIE_SECURE = False     # Set True when HTTPS is enabled

STATIC_ROOT = BASE_DIR / 'staticfiles'
