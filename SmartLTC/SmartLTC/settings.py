"""
Django settings for SmartLTC project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yez_iw0%f!js+^owvu!lce$*0ej1soy1o3h&h1ez&+*@koys^('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'CompanyApp',
    'DriverApp',
    'DeliveryApp',
    'User',
    'QRcode',
    'rest_framework',
    'rest_framework.authtoken',
    'django_rest_passwordreset',
    'knox',
    'location_field.apps.DefaultConfig',
    # 'django_countries'
]
# AUTH_USER_MODEL = 'User.User'
# AUTH_USER_MODEL = 'users.CustomUser'
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':('rest_framework.permissions.AllowAny',),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.pagination.PageNumberPagination',
        # 'rest_framework.permissions.IsAuthenticated',
        'knox.auth.TokenAuthentication',

    ],

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
    # 'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
REST_AUTH_SERIALIZERS = {
'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer',
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SmartLTC.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'SmartLTC.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DeliverApp',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# Managing media
# MEDIA_ROOT  = os.path.join(BASE_DIR, '/media/')
# MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# password_reset email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_SSL=False
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'test.dynamic@gmail.com'
EMAIL_HOST_PASSWORD = '1u1YA551'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'test.dynamic@gmail.com'

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# LOGGING ={
# 'version':1,
# 'loggers':{
#     'django':{
#         'handlers':['file','file2'],
#         'level':'DEBUG'
#     }
# },
# 'handlers':{
#     'file':{
#         'level':'INFO',
#         'class': 'logging.FileHandler',
#         'filename': 'dataflair-debug2.log',
#         'formatter':'simpleRe',
#
#     },
#     'file2':{
#         'level':'DEBUG',
#         'class': 'logging.FileHandler',
#         'filename': 'dataflair-debug3.log',
#         'formatter':'simpleRe',
#         # 'maxBytes': 15728640,  # 1024 * 1024 * 15B = 15MB
#         # 'backupCount': 10,
#
#     }
# },
# 'formatters':{
#     'simpleRe': {
#         'format': '{levelname} {asctime} {module} {message} {levelno} ',
#         # '[%(asctime)s] %(levelname)s %(module)s %(message)s %(user)s'
#         'style': '{',
#
#     }
#
# } }
# MEDIA_URL ='/media/'
# MEDIA_ROOT =os.path.join(os.path.dirname(
#     BASE_DIR),"media_root")

# LOCATION_FIELD = {
# 'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
# 'provider.google.api_key': '<PLACE YOUR API KEY HERE>',
# 'provider.google.api_libraries': '',
# 'provider.google.map.type': 'ROADMAP',
# }
LOCATION_FIELD = {
'map.provider': 'openstreetmap',
'search.provider': 'nominatim',
}
