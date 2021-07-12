from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User


from applications.finder.models import Domain, Provider
from applications.finder.serializers import DomainSerializer, ProviderSerializer


class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all().select_related('provider')
    serializer_class = DomainSerializer

    @action(detail=True)
    #permission_classes=(permissions.IsAdminUser,)
    def highlight(self, request, *args, **kwargs):
        domain = self.get_object()
        return Response(domain.highlighted)

    @action(detail=True,
            methods=['post'])
    def perform_create(self, serializer):
        serializer.save()


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    @action(detail=True)
    def highlight(self, request, *args, **kwargs):
        provider = self.get_object()
        return Response(provider.highlighted)

    def perform_create(self, serializer):
        serializer.save()
