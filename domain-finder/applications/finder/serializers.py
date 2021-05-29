from rest_framework import serializers

from applications.finder.models import Domain, Provider


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        exclude = ['update_at', 'created_at']


class DomainSerializer(serializers.ModelSerializer):
    #provider = ProviderSerializer()
    #provider = serializers.CharField(source="provider.ip_address", read_only=True)

    class Meta:
        model = Domain
        fields = ['id', 'domain', 'provider']
