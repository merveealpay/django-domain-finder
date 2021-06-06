from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.viewsets import ModelViewSet

from applications.finder.models import Domain, Provider
from applications.finder.serializers import DomainSerializer, ProviderSerializer


class DomainViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Domain.objects.all().select_related('provider')
    serializer_class = DomainSerializer

    @action(detail=True)
    def highlight(self, request, *args, **kwargs):
        domain = self.get_object()
        return Response(domain.highlighted)

    def perform_create(self, serializer):
        serializer.save()


class ProviderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    @action(detail=True)
    def highlight(self, request, *args, **kwargs):
        provider = self.get_object()
        return Response(provider.highlighted)

    def perform_create(self, serializer):
        serializer.save()
