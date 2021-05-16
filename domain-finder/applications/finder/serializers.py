from rest_framework import serializers

from applications.finder.models import Domain, Provider


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = ['id', 'country', 'ip_address']


class DomainSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer(read_only=True)
    # TODO bu providerin sadece country'si alınacak.

    class Meta:
        model = Domain
        fields = ['id', 'domain', 'provider']
