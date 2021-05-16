from config.settings.base import *

DEBUG = True
#ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.get(DATABASE_NAME, default=name), #örnek, alttakileri de bu sekilde yap.
        'USER': 'domainadmin',
        'PASSWORD': '1234',
        'HOST': 'db',
        'PORT': 5432,
    }
}