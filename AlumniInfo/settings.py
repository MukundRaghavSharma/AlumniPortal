"""
Django settings for AlumniInfo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os.path
from social_auth.backends import get_backend

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import getpass

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'osxsijds1l!9ae=@g18n4s14s^)^6%h1tp!*my(4%f@u3yzy78'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Alumni',
    'social_auth',
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

AUTHENTICATION_BACKENDS = (
  #'social_auth.backends.contrib.linkedin.LinkedinBackend',
  'social_auth.backends.contrib.github.GithubBackend'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
    'social_auth.context_processors.social_auth_by_type_backends',
)

SOCIAL_AUTH_UID_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
SOCIAL_AUTH_ENABLED_BACKENDS = ('github',)
SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'

#LINKEDIN_SCOPE = ['r_basicprofile', 'r_emailaddress',]
#LINKEDIN_CONSUMER_KEY = 'xxxx' # The LinkedIn application "API Key"
#LINKEDIN_CONSUMER_SECRET = 'xxxx' # The LinkedIn application "Secret Key"

GITHUB_APP_ID = '400b129b1135d29f43e7' 
GITHUB_API_SECRET = '390d0bc723659da4aa4bcd2390f79d2774f58c21'

ROOT_URLCONF = 'AlumniInfo.urls'

WSGI_APPLICATION = 'AlumniInfo.wsgi.application'

LOGIN_URL = '/'

LOGIN_REDIRECT_URL = '/dashboard/'
LOGIN_ERROR_URL = '/login-error/'

MEDIA_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Alumni', 'media')

MEDIA_URL = '/Alumni/media/'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''

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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Alumni', 'static')
