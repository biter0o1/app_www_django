from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Osoby.models import Osoba
from .models import Druzyna
from Osoby.serializers import DruzynaSerializer, OsobaSerializer


@api_view(['GET', 'POST'])
def druzyna_list(request):
    if request.method == 'GET':
        druzyny = Druzyna.objects.all()
        serializer = DruzynaSerializer(druzyny, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DruzynaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def druzyna_detail(request, pk):
    try:
        druzyna = Druzyna.objects.get(pk=pk)
    except Druzyna.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        druzyna = Druzyna.objects.get(pk=pk)
        serializer = DruzynaSerializer(druzyna)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        druzyna.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@permission_classes([IsAuthenticated])
class druzynaIdOsoba(APIView):
    def get(self, request, pk, format=None):
        osoby = Osoba.objects.filter(druzyna_id=pk)
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)