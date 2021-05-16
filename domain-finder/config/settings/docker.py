from config.settings.base import *

DEBUG = True
#ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'domainfinder',
        'USER': 'domainadmin',
        'PASSWORD': '1234',
        'HOST': 'db',
        'PORT': 5432,
    }
}