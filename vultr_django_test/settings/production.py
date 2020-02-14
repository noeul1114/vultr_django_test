from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ["MYSQL_DATABASE"],
        'USER': os.environ["MYSQL_USER"],
        'PASSWORD': os.environ["MYSQL_PASSWORD"],
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}