from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Osoba
from .permissions import IsOwnerOrReadOnly
from .serializers import OsobaSerializer

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class OsobaGet(APIView):
    def get(self, request, format=None):
        if not request.user.has_perm('Osoby.view_osoba'):
            raise PermissionDenied()
        osoby = Osoba.objects.all()
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)

@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class OsobaCreate(APIView):
    def post(self, request, format=None):
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OsobaGetOne(APIView):
    def get_object(self, pk):
        try:
            return Osoba.objects.get(pk=pk)
        except Osoba.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        osoba = self.get_object(pk)
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)


@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class OsobaUpdate(APIView):
    def get_object(self, pk):
        try:
            return Osoba.objects.get(pk=pk)
        except Osoba.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        osoba = self.get_object(pk)
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated, IsOwnerOrReadOnly])
class OsobaDelete(APIView):
    def get_object(self, pk):
        try:
            return Osoba.objects.get(pk=pk)
        except Osoba.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        osoba = self.get_object(pk)
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)
    def delete(self, request, pk, format=None):
        osoba = self.get_object(pk)
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# @api_view(['GET'])
# def osoba_list(request):
#     """
#     Lista wszystkich obiektów modelu Person.
#     """
#     if request.method == 'GET':
#         if request.query_params.get('name'):
#             osoby = Osoba.objects.filter(imie__icontains=request.query_params.get('name'))
#         else:
#             osoby = Osoba.objects.all()
#         serializer = OsobaSerializer(osoby, many=True)
#         return Response(serializer.data)
#
#
#
# @api_view(['POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def osoba_create(request):
#     if request.method == 'POST':
#         serializer = OsobaSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
# @api_view(['GET', 'DELETE'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def osoba_detail(request, pk):
#     """
#     :param request: obiekt DRF Request
#     :param pk: id obiektu Person
#     :return: Response (with status and/or object/s data)
#     """
#     try:
#         osoba = Osoba.objects.get(pk=pk)
#     except Osoba.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = OsobaSerializer(osoba)
#         return Response(serializer.data)
#
#     if request.method == 'DELETE':
#         osoba.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)