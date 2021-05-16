from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from applications.finder.models import Domain, Provider
from applications.finder.serializers import DomainSerializer, ProviderSerializer


class DomainView(APIView):

    def get(self, request, *args, **kwargs):
        domains = Domain.objects.all()
        serializer = DomainSerializer(domains, many=True)
        return Response(serializer.data)

    def post(self):
        # TODO domaini alıncak. domaini dbye kaydetceksin.
        #  response olarak 201 mı doncez, yanında data doncek mıyız?

        pass

    def delete(self):
        # TODO domaini db'den silecegiz, resp ne doncez bak.
        pass


class ProviderView(APIView):

    def get(self, request, *args, **kwargs):
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)
