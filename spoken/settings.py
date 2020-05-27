"""
Django settings for spoken project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
from os.path import *
from .config import *
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SCRIPT_URL = SCRIPT_URL
STVIDEOS_DIR = STVIDEOS_PATH
SEARCH_INDEX_DIR = os.path.join(BASE_DIR, INDEX_PATH)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qoeg0cta8pi$#a7i8t(ufzndy)50e+l465rm7y-k@lvt(s2yae'

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
)
# email errors and 404
SERVER_EMAIL = 'error-report@spoken-tutorial.org'
ADMINS = (
    ('Web Administrator', 'web-notify@spoken-tutorial.org'),
)

MANAGERS = (
    ('Web Administrator', 'web-notify@spoken-tutorial.org'),
)

ADMINISTRATOR_EMAIL = ADMINISTRATOR_EMAIL

NO_REPLY_EMAIL = 'no-reply@spoken-tutorial.org'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEBUG_MODE

COMPRESS_ENABLED = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.redirects',
    'django.contrib.sitemaps',
    'django_extensions',
    'widget_tweaks',
    'captcha',
    'nicedit',
    'report_builder',
    'compressor',
    'forums',
    'cms',
    'creation',
    'statistics',
    'cdcontent',
    'events',
    'mdldjango',
    'youtube',
    'reports',
    'team',
    'certificate',
    'api',
    'rest_framework',
    'workshop',
    'django_filters',
    'impersonate',
    'corsheaders',
    'ckeditor',
    'cron',
    'logs',
    'django_user_agents',
]


ROOT_URLCONF = 'spoken.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'static')], # templates
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

WSGI_APPLICATION = 'spoken.wsgi.application'

# for django.contrib.sites
SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': '',                            # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',    
    
    },
        'moodle': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': MDB,                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': MDB_USER,
        'PASSWORD': MDB_PASS,
        'HOST': MDB_HOST,                  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                  # Set to empty string for default.
    },
    # 'cdeep': {
    #     'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    #     'NAME': CDB,                      # Or path to database file if using sqlite3.
    #     # The following settings are not used with sqlite3:
    #     'USER': CDB_USER,
    #     'PASSWORD': CDB_PASS,
    #     'HOST': '',                  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
    #     'PORT': '',                  # Set to empty string for default.
    # },
    # 'workshop_info': {
    #     'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    #     'NAME': WDB,                      # Or path to database file if using sqlite3.
    #     # The following settings are not used with sqlite3:
    #     'USER': WDB_USER,
    #     'PASSWORD': WDB_PASS,
    #     'HOST': '',                  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
    #     'PORT': '',                  # Set to empty string for default.
    # },
    'forums': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': FDB,                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': FDB_USER,
        'PASSWORD': FDB_PASS,
        'HOST': '',                  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                  # Set to empty string for default.
    },
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

CONN_MAX_AGE = 100

#events settings
ONLINE_TEST_URL = ONLINE_TEST_URL
KEEP_LOGGED_DURATION = 604800
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/') # Absolute path to the media.

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = BASE_DIR + '/static/'

STATIC_URL = '/static/'

COMPRESS_ROOT = STATIC_ROOT
COMPRESS_URL = STATIC_URL

# TEMPLATE_DIRS = (
#     # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
#     # Always use forward slashes, even on Windows.
#     # Don't forget to use absolute paths, not relative paths.
#     BASE_DIR + '/static/',
# )

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #BASE_DIR + '/static/',
)

#debugging
#INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar',)
INTERNAL_IPS = ('127.0.0.1',)

#Moodle Auth
#AUTH_USER_MODEL = 'mdldjango.Users'
DATABASE_ROUTERS = [
    'mdldjango.router.MdlRouter',
    'cdeep.router.CdeepRouter',
    'workshop.router.WorkshopRouter',
    'forums.router.ForumsRouter',
]
#AUTHENTICATION_BACKENDS = ( 'mdldjango.backend.MdlBackend', )

# Login using username or email address
AUTHENTICATION_BACKENDS = (
    'cms.backends.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend'
)
# Reports
REPORT_BUILDER_INCLUDE = []
REPORT_BUILDER_EXCLUDE = ['user']  # Allow all models except User to be accessed
REPORT_BUILDER_ASYNC_REPORT = False

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request"
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_CSS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
)
"""CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }
}"""


# Cache setting for django_user_agents
# Cache backend is optional, but recommended to speed up user agent parsing
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Name of cache backend to cache user agents. If it not specified default
# cache alias will be used. Set to `None` to disable caching.
USER_AGENTS_CACHE = 'default'

HTML_MINIFY = HTML_MINIFY
RECAPTCHA_PUBLIC_KEY = '6Le8qf8SAAAAABV9wYBW99Jotv-EygJXIhMa_n54'
RECAPTCHA_PRIVATE_KEY = '6Le8qf8SAAAAAF9CkucURPapw2vaDPrU4qMzfg73'

#RECAPTCHA V2
GOOGLE_RECAPTCHA_SITE_KEY = GOOGLE_RECAPTCHA_SITE_KEY
GOOGLE_RECAPTCHA_SECRET_KEY = GOOGLE_RECAPTCHA_SECRET_KEY
GOOGLE_RECAPTCHA_SITEVERIFY = GOOGLE_RECAPTCHA_SITEVERIFY
CHANNEL_KEY = CHANNEL_KEY
RECAPTCHA_USE_SSL = True
ACADEMIC_DURATION = 5
SPOKEN_HASH_SALT = 'change this value'


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    #'masquerade.middleware.MasqueradeMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

GEOIP_PATH  = BASE_DIR + '/geodb/'
CORS_ORIGIN_ALLOW_ALL = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'localhost:11211',
        'TIMEOUT': 3600 * 24,
    }
}

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

CRON_ROOT = os.path.join(MEDIA_ROOT, 'emails/')

CKEDITOR_CONFIGS = {
    'default': {
        'height': 150,
        'width': 600,
        'toolbar': 'Full',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['TextColor', 'BGColor'],
            [ 'Source']
        ]
    }
}

ANALYTICS_DATA = ''

SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # required for checking returning visits

SAVE_LOGS_WITH_CELERY = True

MONGO_BULK_INSERT_COUNT = 10000