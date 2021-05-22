from rest_framework import serializers

from applications.finder.models import Domain, Provider


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'


class DomainSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer(read_only=True)
    #provider_id = serializers.PrimaryKeyRelatedField(read_only=True)
    #provider = serializers.CharField(source="provider.ip_address", read_only=True)

    class Meta:
        model = Domain
        fields = '__all__'
