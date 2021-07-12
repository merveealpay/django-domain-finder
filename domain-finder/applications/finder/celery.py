from __future__ import absolute_import
import os
from celery import Celery

import config
from config.settings import base
from .domain_crawler import DomainList

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
app = Celery('applications.finder')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: base.INSTALLED_APPS)


@app.task(bind=True)
def crawl_domain():
    DomainList.handle()
