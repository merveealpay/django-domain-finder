from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from applications.finder.models import Domain, Provider
from applications.finder.serializers import DomainSerializer, ProviderSerializer


class DomainView(APIView):

    def get(self, request, *args, **kwargs):
        domains = Domain.objects.all()
        serializer = DomainSerializer(domains.prefetch_related('provider'), many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = DomainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProviderView(APIView):

    def get(self, request, *args, **kwargs):
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProviderDetailView(APIView):

    def get_object(self, pk):
        try:
            return Provider.objects.get(pk=pk)
        except Provider.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        provider = self.get_object(pk)
        serializer = ProviderSerializer(provider)
        return Response(serializer.data)

    def delete(self, request, pk):
        provider = self.get_object(pk)
        provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DomainDetailView(APIView):

    def get_object(self, pk):
        try:
            return Domain.objects.get(pk=pk)
        except Domain.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        domain = self.get_object(pk)
        serializer = DomainSerializer(domain)
        return Response(serializer.data)

    def delete(self, request, pk):
        domain = self.get_object(pk)
        domain.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
