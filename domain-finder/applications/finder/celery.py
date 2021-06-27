from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from django.core import management

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
app = Celery('applications.finder')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))

@app.task(bind=True)
def take_domains():
    try:
        print("in celery module")
        management.call_command("domain_crawler", verbosity=0)
        return "success"

    except:
        print("error")
