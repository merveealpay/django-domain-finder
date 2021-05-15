from config.settings.base import *

DEBUG = True
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'domainfinder',
        'USER': 'domainadmin',
        'PASSWORD': '1234',
        #'HOST': 'localhost'
        'HOST': 'db',
        'PORT': 5432,
    }
}