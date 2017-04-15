import os
ALLOWED_HOSTS = ['0.0.0.0:8000', '*']

DATABASES_HOST = os.getenv('DATABASES_HOST', '')
PASSWORD_DATABASES = os.getenv('PASSWORD_DATABASES', '')

DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'lowcost',
            'USER': 'myroslav',
            'PASSWORD': PASSWORD_DATABASES,
            'HOST': DATABASES_HOST,
            'PORT': '5432',
        }
    }

DEBUG = False