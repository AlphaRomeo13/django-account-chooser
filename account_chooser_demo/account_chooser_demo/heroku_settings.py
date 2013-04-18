from account_chooser_demo.account_chooser_demo.common_settings import *

DEBUG = True

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

ROOT_URLCONF = 'account_chooser_demo.account_chooser_demo.urls'
WSGI_APPLICATION = 'account_chooser_demo.wsgi.application'
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

