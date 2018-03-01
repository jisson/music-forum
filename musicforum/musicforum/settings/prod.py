from .base import *


# WEBDAV MEDIA STORAGE
# ------------------------------------------------------------------------------
# See: http://django-webdav-storage.readthedocs.io/en/latest/
DEFAULT_FILE_STORAGE = 'django_webdav_storage.storage.WebDavStorage'
WEBDAV_URL = env.str('DJANGO_WEBDAV_URL')
WEBDAV_PUBLIC_URL = env.str('DJANGO_WEBDAV_PUBLIC_URL')


# EMAILS
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env.str('DJANGO_EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
