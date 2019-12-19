"""
Django settings for conf project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kh+xixf!!o^ef%=o89oh4bf+dm#6-5n8ao=o8w^+ii18)3hi_='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ADMINS = (('sila', 'silatchomsiaka@gmail.com'),)
TESTING = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.webdesign',
    'django.contrib.humanize',

    #Third parties
    'djangotoolbox',
    'django_user_agents',
    'ajaxuploader',

    'ikwen.core',
    'ikwen.accesscontrol',
    'ikwen.billing',
    'ikwen.flatpages',
    'ikwen.cashout',
    'ikwen.partnership',
    'ikwen.theming',
    'ikwen.rewarding',

    'ikwen_webnode.web',
    'ikwen_webnode.webnode',
    'ikwen_webnode.items',
    'ikwen_webnode.blog',

    'ikwen_foulassi.foulassi',
    'ikwen_foulassi.reporting',
    'ikwen_foulassi.school',

    'ikwen_kakocase.kakocase',
    'ikwen_kakocase.kako',

    # 'dbbackup',
    'echo',
    'website',
    'tsunami',
    'smartevent',
    'daraja',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    'ikwen.core.context_processors.project_settings',
    'ikwen.billing.context_processors.payment_means',
)

ROOT_URLCONF = 'conf.urls'

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


WALLETS_DB_ALIAS = "wallets"

if DEBUG or TESTING :
    WALLETS_DB = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/silatchom/Dropbox/PycharmProjects/ikwenWebsite/db.sqlite3',
    }
else:
    WALLETS_DB = {  # ikwen_kakocase.ikwen_kakocase relational database used to store sensitive objects among which CashOutRequest
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': ''
    }

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'smartevent',
    },
    'umbrella': {
        'ENGINE': 'django_mongodb_engine', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ikwen_umbrella',
    },
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

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
    # '/home/silatchom/Dropbox/PycharmProjects/ikwenWebsite/templates/',
)


#  ***       IKWEN CONFIGURATION       ***      #

IS_IKWEN = True

IS_UMBRELLA = True

SITE_ID = '54eb6d3379b531e09cb3704b'

IKWEN_SERVICE_ID = '5df037ef62ea542dfb018426'


PROJECT_NAME = 'SmartEvent'

PROJECT_URL = 'http://localhost'

AUTH_USER_MODEL = 'accesscontrol.Member'

AUTHENTICATION_BACKENDS = (
    'permission_backend_nonrel.backends.NonrelPermissionBackend',
    'ikwen.accesscontrol.backends.LocalDataStoreBackend',
)

MEMBER_AVATAR = 'ikwen/img/member-avatar.jpg'

# BILLING SETTINGS


PAYMENTS = {
    'default': {
        'before': 'ikwen.billing.collect.set_invoice_checkout',
        'after': 'ikwen.billing.collect.confirm_invoice_payment'
    },
    'tsunami': {
        'before': 'tsunami.views.set_checkout',
        'after': 'tsunami.views.confirm_checkout'
    }
}
MTN_MOMO_API_URL = 'https://developer.mtn.cm/OnlineMomoWeb/faces/transaction/transactionRequest.xhtml'
ORANGE_MONEY_API_URL = 'https://api.orange.com/orange-money-webpay/cm/v1'
OM_FEES_ON_MERCHANT = True


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/home/silatchom/Dropbox/PycharmProjects/SmartEvent/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/smartevent/'
# http://localhost/media/daraja/



