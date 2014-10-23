"""
Django settings for TreaProject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import APPEND_SLASH


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIR = BASE_DIR + '/templates/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ww3=fhba78p=6byoo8n%@ocfuaamkbn!8+i0m$iq!k8t551r+1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

COMPRESS_ENABLED = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

LOGIN_URL = "login"
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'dynamicForms',
    'south',
    'sekizai',
    'compressor',
)

MIDDLEWARE_CLASSES = (
    'dynamicForms.middlets.ValidationErrorToHttpErrorMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'TreaProject.urls'

WSGI_APPLICATION = 'TreaProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'mydb',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'trea',
            'PASSWORD': 'trea123',
            'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/home/nahu/git/django-survey/TreaProject/dynamicForms/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

FIELD_FILES = (
    'dynamicForms.fieldtypes.TextField',
    'dynamicForms.fieldtypes.TextAreaField',
    'dynamicForms.fieldtypes.EmailField',
    'dynamicForms.fieldtypes.CheckboxField',
    #CHECKBOX_MULTIPLE: 'dynamicForms.fieldtypes.MultipleChoiceField',
    'dynamicForms.fieldtypes.SelectField',
    #SELECT_MULTIPLE: 'dynamicForms.fieldtypes.MultipleChoiceField',
    #RADIO_MULTIPLE: 'dynamicForms.fieldtypes.ChoiceField',
    #DATE: 'dynamicForms.fieldtypes.DateField',
    'dynamicForms.fieldtypes.NumberField',
    #URL: 'dynamicForms.fieldtypes.URLField',
    'dynamicForms.fieldtypes.CIField',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'sekizai.context_processors.sekizai',
)