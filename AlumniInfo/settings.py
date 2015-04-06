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

#from perms import MyAdaptorEditInline

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

ALLOWED_HOSTS = ['128.237.170.178']

SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

ENDLESS_PAGINATION_LOADING = """<img src="/static/images/loading.gif" alt="loading" />"""


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Alumni',
    'endless_pagination',
    'ajaximage',
    #'social.apps.django_app.default',
    # 'django_wysiwyg',
    'easy_thumbnails',
    'image_cropping',
    'inplaceeditform',
    'inplaceeditform_extra_fields',
)

AJAXIMAGE_AUTH_TEST = lambda u: True

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

class MyAdaptorEditInline(object):

    @classmethod
    def can_edit(cls, adaptor_field):
        user = adaptor_field.request.user
        obj = adaptor_field.obj
        can_edit = False
        if user.is_anonymous():
            pass
        elif user.is_superuser:
            can_edit = True
        else:
           can_edit = has_permission(obj, user, 'edit')
        return can_edit

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


LOGIN_URL = '/'

LOGIN_REDIRECT_URL = '/dashboard/'

MEDIA_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Alumni', 'media')

MEDIA_URL = '/Alumni/media/'

#SOCIAL_AUTH_URL_NAMESPACE = 'social'

INPLACEEDIT_EVENT = "click"
INPLACE_ENABLE_CLASS = 'enable'
INPLACEEDIT_EDIT_EMPTY_VALUE = 'Click to edit'

# ADAPTOR_INPLACEEDIT_EDIT = 'AlumniInfo.fields.MyAdaptor'


# ADAPTOR_INPLACEEDIT = {'textarea': 'inplaceeditform_extra_fields.fields.AdaptorTinyMCEField',
#                        #'textarea': 'inplaceeditform_extra_fields.fields.AdaptorSimpleTinyMCEField',
#                        'image': 'inplaceeditform_extra_fields.fields.AdaptorImageThumbnailField',
#                        'fk': 'inplaceeditform_extra_fields.fields.AdaptorAutoCompleteForeingKeyField',
#                        'm2mcomma': 'inplaceeditform_extra_fields.fields.AdaptorAutoCompleteManyToManyField'}

# ADAPTOR_INPLACEEDIT = {'auto_fk': 'inplaceeditform_extra_fields.fields.AdaptorAutoCompleteForeingKeyField',
#                        'auto_m2m': 'inplaceeditform_extra_fields.fields.AdaptorAutoCompleteManyToManyField',
#                        'image_thumb': 'inplaceeditform_extra_fields.fields.AdaptorImageThumbnailField',
#                        'tiny': 'inplaceeditform_extra_fields.fields.AdaptorTinyMCEField',
#                        'tiny_simple': 'inplaceeditform_extra_fields.fields.AdaptorSimpleTinyMCEField'}

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



# Stuff for Heroku #
'''
# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
'''
