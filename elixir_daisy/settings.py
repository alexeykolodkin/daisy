"""
Django settings for elixir_daisy project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

import pytz

COMPANY = 'LCSB'  # Used for generating some models' verbose names


AUTH_USER_MODEL = 'core.User'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qe1lmt43v1n%66vibs0&0s9qw7i!xjs^!i#f#$t_7-r8n&=+sp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'stronghold',
    'guardian',
    'formtools',
    'widget_tweaks',
    'core.apps.CoreConfig',
    'web.apps.WebConfig',
    'notification.apps.NotificationConfig',
    'django.contrib.admin',
    'debug_toolbar',
    'django_celery_results',
    'django_celery_beat',
    'celery_haystack',
    'sequences.apps.SequencesConfig'
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'stronghold.middleware.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'elixir_daisy.urls'

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

WSGI_APPLICATION = 'elixir_daisy.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Authentication backend
# https://django-guardian.readthedocs.io/en/stable/configuration.html

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
]

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Luxembourg'
TZINFO = pytz.timezone(TIME_ZONE)

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static/'

INTERNAL_IPS = '127.0.0.1'

# EMAIL settings
# https://docs.djangoproject.com/en/2.0/topics/email/
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_DONOTREPLY = 'do-not-reply@daisy.lcsb.uni.lu'

# server settings
SERVER_SCHEME = 'https'
SERVER_URL = 'example.com'

# LOGGING settings
# https://docs.djangoproject.com/en/2.0/topics/logging/
LOGFILE_MAX_BYTES = 16777216  # 16MB
LOG_DIR = os.path.join(BASE_DIR, 'log')
LOG_LEVEL = DEBUG and 'DEBUG' or 'ERROR'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'sql': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': LOGFILE_MAX_BYTES,
            'backupCount': 10,
            'filters': ['require_debug_true'],
            'filename': os.path.join(LOG_DIR, 'daisy.sql.log'),
            'formatter': 'verbose'
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': LOGFILE_MAX_BYTES,
            'backupCount': 10,
            'filename': os.path.join(LOG_DIR, 'daisy.log'),
            'formatter': 'verbose'
        },
        'templates': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': LOGFILE_MAX_BYTES,
            'backupCount': 1,
            'filters': ['require_debug_true'],
            'filename': os.path.join(LOG_DIR, 'daisy.template_errors.log'),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['mail_admins', 'console', 'logfile'],
            'propagate': True,
            'level': LOG_LEVEL,
        },
        'django.request': {
            'handlers': ['mail_admins', 'console', 'logfile'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
        'django.template': {
            'handlers': ['templates'],
            'propagate': False,
            'level': LOG_LEVEL,
        },
        'django.db.backends': {
            'handlers': ['mail_admins', 'sql'],
            'propagate': False,
            'level': LOG_LEVEL,
        },
        'daisy': {
            'handlers': ['mail_admins', 'console', 'logfile'],
            'level': LOG_LEVEL,
            'propagate': True,
        }
    }
}

# search settings
FACET_FIELDS = {
    'dataset': (
        'local_custodians',
        'consent_status',
        'data_types',
        'deidentification_method',
        'is_published',
    ),
    'contract': (
        'company_roles',
        'contacts',
        'partners',
        'project',
        'has_legal_documents',
    ),
    'project': (
        'local_custodians',
        'start_year',
        'end_year',
        'disease_terms',
        'study_terms',
        'phenotype_terms',
        'gene_terms',
        'has_cner',
        'has_erp',
        'has_legal_documents',
        'funding_sources',
        'company_personnel',
        'contacts',

    ),
    'cohort': (
        "owners",
        "institutes"
    ),
    'partner': (
        "geo_category",
        "sector_category",
        "is_clinical"
    ),
    'contact': (
        "type",
        "partners"
    )
}

# by default, notifications by email are disabled
NOTIFICATIONS_DISABLED = True

LOGIN_USERNAME_PLACEHOLDER = ''
LOGIN_PASSWORD_PLACEHOLDER = ''

# Import local settings to override those values based on the deployment environment
try:
    from .settings_local import *
except ImportError as e:
    pass
