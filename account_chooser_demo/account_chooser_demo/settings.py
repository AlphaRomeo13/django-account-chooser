# Django settings for account_chooser_demo project.
import os
import sys
import imp
import django.conf.global_settings as DEFAULT_SETTINGS

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     os.path.pardir, os.path.pardir))
sys.path.append(PROJECT_DIR)

ON_OPENSHIFT = False
if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    ON_OPENSHIFT = True

print PROJECT_DIR
default_keys = {'SECRET_KEY':
                '=i8bda@yme_b(j=r20*lnf36lnu3@c4fdhdqmjw42&amp;jw&amp;9f_v'}

if ON_OPENSHIFT:
    DEBUG = False
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dfdma6i9i1pm3i',
        'HOST': 'ec2-23-21-203-9.compute-1.amazonaws.com',
        'PORT': 5432,
        'USER': 'waalzkeqfqkqqr',
        'PASSWORD': 'dgx2KCQw7HYsglBD2JOqwxH1Iv'
        }
    }
    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

    imp.find_module('account_chooser_demo/openshiftlibs')
    import openshiftlibs
    use_keys = openshiftlibs.openshift_secure(default_keys)

    MEDIA_ROOT = os.environ.get('OPENSHIFT_DATA_DIR', '')
    STATIC_ROOT = os.path.join(PROJECT_DIR, '..', 'static')

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',
        'django.contrib.admindocs',

        'registration',  # provide signup, login views for demo
        'django_facebook',
        'south',

        'account_chooser',
        'demo',
  )

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'account_chooser.middleware.AccountChooserMiddleware',
  )

else:
    DEBUG = True
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'account_chooser.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
    }
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    use_keys = default_keys

    MEDIA_ROOT = 'media/'
    STATIC_ROOT = 'static/'

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',
        'django.contrib.admindocs',

        'registration',  # provide signup, login views for demo
        'django_facebook',
        'django_extensions',
        'debug_toolbar',
        'south',

        'account_chooser',
        'demo',
  )

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'account_chooser.middleware.AccountChooserMiddleware',
    )

    INTERNAL_IPS = ('127.0.0.1',)
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'TAG': 'html',
    }

ROOT_URLCONF = 'account_chooser_demo.urls'

SECRET_KEY = use_keys['SECRET_KEY']

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


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
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# facebook settings
TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django_facebook.context_processors.facebook',
)

AUTHENTICATION_BACKENDS = (
    'django_facebook.auth_backends.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_PROFILE_MODULE = 'registration.registrationprofile'
#TODO: configure LOGIN_REDIRECT_URL
LOGIN_REDIRECT_URL = '/'

ACCOUNT_CHOOSER_SETTINGS = {
                        'signupUrl': '/accounts/register/',
                        'siteEmailId': 'id_email',
                        'sitePasswordId': 'id_password',
                        'siteDisplayNameId': 'id_username',
                        'sitePhotoUrlId': '',
                        'providers': {
                                      "facebook.com": '/facebook/connect',
                                      "twitter.com": '/twitter_auth',
                                      "google.com.com": '/gplus_auth',
                                      },
}

ACCOUNT_ACTIVATION_DAYS = 7


#face book settings
FACEBOOK_APP_ID = "422724461106816"
FACEBOOK_APP_SECRET = "0bc28668441234924b6031faee86408b"
FACEBOOK_REGISTRATION_BACKEND = 'registration_backends.DjangoRegistrationDefaultBackend'

# twitter settings
CONSTUMER_KEY       = "v8wsuWmpbmoKX7IPfEr49A"
CONSTUMER_SECRET    = "CcoXqIKiyXXzapOKQ8Rq2QBT8NSPU9GpMzTtaiCZs"
ACCESS_TOKEN        = '200993161-8ortaWA9zpJXY0fu9nKotldSPykHy0C6eWXgQlV7'
ACCESS_SECRET       = 'KUC6uQuufk68eJH124Gv6aVcFiB34QVepmVgpgmJg4'
CALLBACK            = "http://account-chooser-demo.herokuapp.com/demo/twitter_callback/"

#gplus_settings
CLIENT_ID       ="308413983615.apps.googleusercontent.com"
CLIENT_SECRET   ="GboICNuFvxGbB679f0hUNbRl"
SCOPE           ='https://www.googleapis.com/auth/plus.login'
REDIRECT_URI    ='http://localhost:8000/gplus_callback'

MODE = 'django_registration'
