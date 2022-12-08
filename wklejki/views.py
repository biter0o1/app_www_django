from django.http import HttpResponse, Http404
from django_filters import filters
from django_filters import rest_framework as filters
from rest_framework import status, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from . import permission
from .models import Wklejki, Kategorie
from .Serializer import WklejkiSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from .permission import IsOwnerOrReadOnly


class Wklejki_list(APIView):

    def get(self, request, format=None):
        if request.query_params.get('kategoria'):
            wklejka = Wklejki.objects.filter(kategoria__icontains=request.query_params.get('kategoria'))
        elif request.query_params.get('najwiecej-lajkow'):
            wklejka = Wklejki.objects.order_by("-lajki")[:int(request.query_params.get('najwiecej-lajkow'))]
        else:
            wklejka = Wklejki.objects.all()
        serializer = WklejkiSerializer(wklejka, many=True)
        return Response(serializer.data)


class Wklejki_utworz(APIView):
    def get(self, request, format=None):
        if request.query_params.get('kategoria'):
            wklejka = Wklejki.objects.filter(kategoria__icontains=request.query_params.get('kategoria'))
        else:
            wklejka = Wklejki.objects.all()
        serializer = WklejkiSerializer(wklejka, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = WklejkiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(wlasciciel_wklejki=None if request.user.is_anonymous else self.request.user, lajki=0)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsOwnerOrReadOnly])
class Wklejki_usun(APIView):
    def get_object(self, pk):
        try:
            return Wklejki.objects.get(pk=pk)
        except Wklejki.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        wklejka = self.get_object(pk)
        serializer = WklejkiSerializer(wklejka)
        return Response(serializer.data)
    def delete(self, request, pk, format=None):
        Wklejki = self.get_object(pk)
        Wklejki.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsOwnerOrReadOnly])
class Wklejki_aktualizacja(APIView):
    def get_object(self, pk):
        try:
            return Wklejki.objects.get(pk=pk)
        except Wklejki.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        Wklejki = self.get_object(pk)
        serializer = WklejkiSerializer(Wklejki)
        return Response(serializer.data)

    def put(self, request, pk, format=None):

        wklejka = self.get_object(pk)
        serializer = WklejkiSerializer(wklejka, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class Wklejki_lajki(APIView):
    def get_object(self, pk):
        try:
            return Wklejki.objects.get(pk=pk)
        except Wklejki.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Wklejki = self.get_object(pk)
        serializer = WklejkiSerializer(Wklejki)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        wklejka = self.get_object(pk)
        wklejka.lajki += 1
        wklejka.save(update_fields=['lajki'])
        return Response(status=status.HTTP_200_OK)
class Wklejki_list_by_user(APIView):

    def get(self, request, pk ,format=None):

        wklejka = Wklejki.objects.filter(wlasciciel_wklejki=pk)
        serializer = WklejkiSerializer(wklejka, many=True)
        return Response(serializer.data)

