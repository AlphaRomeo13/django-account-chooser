from account_chooser_demo.common_settings import *

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

ROOT_URLCONF = 'account_chooser_demo.urls'
WSGI_APPLICATION = 'account_chooser_demo.wsgi.application'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
