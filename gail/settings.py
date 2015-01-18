"""
Django settings for gail project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import dj_database_url
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3u97sn%0lxu!r++q-9my9a+b2g4v_j!%2y_146wx7x3a0mubla'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False 

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
   os.path.join(BASE_DIR, 'templates'),
)

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nutrients',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gail.urls'

WSGI_APPLICATION = 'gail.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gail',
        'USER': 'postgresql',
        'PASSWORD': 'postgresql',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

DATABASES = {'default': dj_database_url.config(default='postgres://foo:bar@localhost:5432/gail')}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

### added 1/14/15

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
#PROJECT_ROOT = os.path.abspath(os.path.dirname(__name__))
STATIC_ROOT= os.path.join(PROJECT_ROOT,'/static/')
# STATIC_ROOT = os.path.join(os.getcwd(),'static')
STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

ADMIN_MEDIA_PREFIX = '/static/admin/'

# heroku run python manage.py collectstatic
# the above ran automatically on deploy.
# puts into static_root

# Parse database configuration from $DATABASE_URL

DATABASES = { 'default' : dj_database_url.config()}
# we only need the engine name, as heroku takes care of the rest
DATABASES = {
     "default": {
         "ENGINE": "django.db.backends.postgresql_psycopg2",
     }
}
#         "NAME": "gail",
######
DATABASES = {'default': dj_database_url.config(default='postgres://postgresql:postgresql@localhost:5432/gail')}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# try to load local_settings.py if it exists
try:
  from local_settings import *
except Exception as e:
  pass

##########  added 1/15

import logging
import logging.config

if DEBUG:
    # will output to your console
    logging.basicConfig(
        level = logging.DEBUG,
        format = '%(asctime)s %(levelname)s %(message)s',
        filename = '/tmp/access.log',
        filemode = 'a'
    )
else:
    # will output to logging file
    logging.basicConfig(
        level = logging.DEBUG,
        format = '%(asctime)s %(levelname)s %(message)s',
        filename = '/tmp/access.log',
        filemode = 'a'
    )

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/debug.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
