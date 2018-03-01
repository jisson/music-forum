from .base import *


# EMAILS
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env.str('DJANGO_EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')
