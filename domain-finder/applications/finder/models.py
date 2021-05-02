from django.db import models

from applications.core.models import TimeStampBaseModel


class Provider(TimeStampBaseModel):
    country = models.CharField(max_length=250)
    ip_address = models.GenericIPAddressField()
    detail = models.TextField(null=True)


class Domain(TimeStampBaseModel):
    domain = models.CharField(max_length=100)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
