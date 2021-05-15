from django.contrib import admin
from .models import Domain, Provider


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ['id', 'domain', 'provider']


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['id', 'country', 'ip_address', 'detail']
