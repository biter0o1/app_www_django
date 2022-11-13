from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Osoba
from .serializers import OsobaSerializer
from rest_framework import permissions


@api_view(['GET'])
def osoba_list(request):
    """
    Lista wszystkich obiektów modelu Person.
    """
    if request.method == 'GET':
        if request.query_params.get('name'):
            osoby = Osoba.objects.filter(imie__icontains=request.query_params.get('name'))
        else:
            osoby = Osoba.objects.all()
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_create(request):
    if request.method == 'POST':
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_detail(request, pk):
    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Person
    :return: Response (with status and/or object/s data)
    """
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)

    if request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)