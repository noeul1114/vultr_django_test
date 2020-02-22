from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8#%po-zjnph17-g)w#!m!1aq%_ggeh!x#89870q1t=p6koj*7p'

DEBUG = False

if DEBUG:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = ["*"]

path = "/run/secrets/"

file = open(path+"MYSQL_DATABASE","r")
MYSQL_DATABASE = file.read()
MYSQL_DATABASE = MYSQL_DATABASE.rstrip().lstrip()
file.close()

file = open(path+"MYSQL_USER","r")
MYSQL_USER = file.read()
MYSQL_USER = MYSQL_USER.rstrip().lstrip()
file.close()

file = open(path+"MYSQL_PASSWORD","r")
MYSQL_PASSWORD = file.read()
MYSQL_PASSWORD = MYSQL_PASSWORD.rstrip().lstrip()
file.close()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': MYSQL_DATABASE,
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASSWORD,
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')