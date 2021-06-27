from celery import shared_task
import celery
import time
from django.core import management


@celery.task
def take_domains():
    try:
        print("in celery module")
        management.call_command("domain_crawler", verbosity=0)
        return "success"

    except:
        print("error")
