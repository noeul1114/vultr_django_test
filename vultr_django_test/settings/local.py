from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8#%po-zjnph17-g)w#!m!1aq%_ggeh!x#89870q1t=p6koj*7p'

DEBUG = True

if DEBUG:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')