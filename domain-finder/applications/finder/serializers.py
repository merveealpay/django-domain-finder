from rest_framework import serializers

from applications.finder.models import Domain, Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        exclude = ['update_at', 'created_at']


class DomainSerializer(serializers.ModelSerializer):
    # provider = ProviderSerializer()
    provider = serializers.CharField(source="provider.ip_address", read_only=True)
    provider_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Domain
        fields = ['id', 'domain', 'provider', 'provider_id']

# class TestSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True)
#     last_name = serializers.CharField(required=False)
