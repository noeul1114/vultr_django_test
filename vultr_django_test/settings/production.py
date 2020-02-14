from .base import *

DEBUG = False

path = "/run/secrets/"

file = open(path+"MYSQL_DATABASE","r")
MYSQL_DATABASE = file.read()
file.close()

file = open(path+"MYSQL_USER","r")
MYSQL_USER = file.read()
file.close()

file = open(path+"MYSQL_PASSWORD","r")
MYSQL_PASSWORD = file.read()
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