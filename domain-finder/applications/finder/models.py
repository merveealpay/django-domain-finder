from django.db import models


class Provider(models.Model):
    country = models.CharField(max_length=250)
    ip_address = models.GenericIPAddressField()
    detail = models.TextField(null=True)
    created_at = models.DateTimeField(auto_created=True)
    update_at = models.DateTimeField(auto_created=True)


class Domain(models.Model):
    domain = models.CharField(max_length=100)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)
    update_at = models.DateTimeField(auto_created=True)
