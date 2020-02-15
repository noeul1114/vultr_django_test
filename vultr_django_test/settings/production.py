from .base import *

DEBUG = False

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