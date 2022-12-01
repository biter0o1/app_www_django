from django.http import HttpResponse, Http404
from django.shortcuts import render
from rest_framework import status

from .models import Wklejki
from .Serializer import WklejkiSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

#cala lista
class Wklejki_list(APIView):
    def get(self, request, format=None):
        wklejka = Wklejki.objects.all()
        serializer = WklejkiSerializer(wklejka,many=True)
        return Response(serializer.data)

class Wklejki_utworz(APIView):
    def post(self, request, format=None):
        serializer = WklejkiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Wklejki_usun(APIView):
    def get_object(self, pk):
        try:
            return Wklejki.objects.get(pk=pk)
        except Wklejki.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Wklejki = self.get_object(pk)
        serializer = WklejkiSerializer(Wklejki)
        return Response(serializer.data)
    def delete(self, request, pk, format=None):
        Wklejki = self.get_object(pk)
        Wklejki.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

        wklejki = self.get_object(pk)
        serializer = WklejkiSerializer(wklejki, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




