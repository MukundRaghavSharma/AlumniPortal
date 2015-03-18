"""
Django settings for AlumniInfo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

import os.path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import getpass

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'osxsijds1l!9ae=@g18n4s14s^)^6%h1tp!*my(4%f@u3yzy78'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
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
    'social.apps.django_app.default',
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
   'django.core.context_processors.request',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
   'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'social.backends.linkedin.LinkedinOAuth',
   'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'AlumniInfo.urls'

WSGI_APPLICATION = 'AlumniInfo.wsgi.application'

LOGIN_URL = '/'

LOGIN_REDIRECT_URL = '/dashboard/'

MEDIA_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Alumni', 'media')

MEDIA_URL = '/Alumni/media/'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

# LinkedIn Stuff #

SOCIAL_AUTH_LINKEDIN_KEY = '75rg300f8mdwnn' 
SOCIAL_AUTH_LINKEDIN_SECRET = 'feGCLy3VQPEGk4Ot'

SOCIAL_AUTH_LINKEDIN_SCOPE = ['r_emailaddress', 'r_fullprofile', 'r_contactinfo']
SOCIAL_AUTH_LINKEDIN_FIELD_SELECTORS = ['email-address', 'headline', 'industry']
SOCIAL_AUTH_LINKEDIN_EXTRA_DATA = [('id', 'id'),
                                   ('firstName', 'first_name'),
                                   ('lastName', 'last_name'),
                                   ('emailAddress', 'email_address'),
                                   ('location', 'location'),
                                   ('headline', 'headline'),
                                   ('positions', 'positions'),
                                   ('summary', 'summary'),
                                   ('public-profile-url', 'public_profile_url'),
                                   ('picture-url', 'picture_url'),
                                   ('industry', 'industry')]

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/signin_2'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'Alumni.views.social_auth_to_profile',
)

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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
