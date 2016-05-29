#! /usr/bin/env python2.7
"""
Django settings for rollbardjangodemo project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import os
import sys

# Django settings for rollbardjangodemo - suitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = (

)

# SECURITY WARNING: keep the secret key used in production secret!
# Make this unique, and don't share it with anybody.
# http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = 'f$#cct0mhiwq5o@3s3a77-=$(h50u^g!i9dpguxd29!@9n=r60'

# Absolute paths for where the project and templates are stored.
ABS_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
ABS_TEMPLATES_PATH = '%s/templates' % ABS_PROJECT_ROOT

# add root directory to PYTHONPATH
if ABS_PROJECT_ROOT not in sys.path:
    sys.path.insert(0, ABS_PROJECT_ROOT)

ADMINS = (
    ('Your Name', 'admin@example.com'),
)
MANAGERS = ADMINS


ROOT_URLCONF = 'rollbardjangodemo.urls'

# Python dotted path to the WSGI application used by Django's runserver.
# disabled - outsite the app
WSGI_APPLICATION = 'rollbardjangodemo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        #'ENGINE': 'django.db.backends.{{ db_engine }}',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rollbardjangodemo',
        # The rest is not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '',
        'CONN_MAX_AGE': 60,
        'HOST': 'localhost',
        'PORT': '',
    }
}

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Application definition
# django debugging stuff
ADMIN_TOOLS = (
)

# django
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'rollbardjangodemo.home',
)

EXTERNAL_APPS = (
    'django_extensions',
    'compressor',
)

# the order is important!
INSTALLED_APPS = ADMIN_TOOLS + DJANGO_APPS + LOCAL_APPS + EXTERNAL_APPS

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in the directory "static-assets/" then do `./manage.py migrate` on
# production.
STATIC_ROOT = '%s/static' % ABS_PROJECT_ROOT
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = '%s/media' % ABS_PROJECT_ROOT

# The URL that handles the media, static, etc.
STATIC_URL = '/static/'
MEDIA_URL = STATIC_URL + 'media/'

# THE REST IS PRETTY MUCH DEFAULT

# Additional locations of static files
STATICFILES_DIRS = (
    '%s/static-assets' % ABS_PROJECT_ROOT,
)


# List of finder classes that know how to find static files in various
# locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = None

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ABS_TEMPLATES_PATH],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
            ],
        },
    },
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
)


ROLLBAR = {
    'access_token': 'c0c9e4316b85498ea02d82b2e313bf34',
    'environment': 'development' if DEBUG else 'production',
    'root': ABS_PROJECT_ROOT,
}


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': [],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

