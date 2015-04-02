"""
Django settings for AlumniInfo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import sys
import os.path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import getpass

if sys.version_info > (3, 0):
    import configparser
else:
    import ConfigParser


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'osxsijds1l!9ae=@g18n4s14s^)^6%h1tp!*my(4%f@u3yzy78'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Alumni',
    #'social.apps.django_app.default',
    'inplaceeditform',
    'django_wysiwyg',
    'easy_thumbnails',
    'image_cropping',
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

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.core.context_processors.request',
   'django.contrib.messages.context_processors.messages',
   #'social.apps.django_app.context_processors.backends',
   #'social.apps.django_app.context_processors.login_redirect',

)

AUTHENTICATION_BACKENDS = (
   #'social.backends.facebook.FacebookOAuth2',
   #'social.backends.google.GoogleOAuth2',
   #'social.backends.twitter.TwitterOAuth',
   #'social.backends.linkedin.LinkedinOAuth',
   'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'AlumniInfo.urls'

WSGI_APPLICATION = 'AlumniInfo.wsgi.application'

LOGIN_URL = '/'

LOGIN_REDIRECT_URL = '/dashboard/'

MEDIA_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Alumni', 'media')

MEDIA_URL = '/Alumni/media/'

#SOCIAL_AUTH_URL_NAMESPACE = 'social'

INPLACEEDIT_EVENT = "click"
INPLACE_ENABLE_CLASS = 'enable'
INPLACEEDIT_EDIT_EMPTY_VALUE = 'Click to edit'

AUTH_PROFILE_MODULE = 'Alumni.Alumni'
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'AlumniPortal',
        'USER': getpass.getuser(), 
        'PASSWORD': 'cmuakpsi',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ALLOWED_HOSTS = ['*']

# Email Information #
if sys.version_info > (3,0):
    config = configparser.ConfigParser()
else:
    config = ConfigParser.ConfigParser()
config.read("config.ini")

EMAIL_HOST = config.get('Email', 'Host')
EMAIL_PORT = config.get('Email', 'Port')
EMAIL_HOST_USER = config.get('Email', 'User')
EMAIL_HOST_PASSWORD = config.get('Email', 'Password')
EMAIL_USE_SSL = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS
