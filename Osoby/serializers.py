from rest_framework import serializers
from .models import Osoba, Druzyna


class OsobaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True)
    nazwisko = serializers.CharField(required=True)
    miesiac_urodzenia = serializers.IntegerField(choices=Osoba.Miesiace, default=Osoba.Miesiace)
    data_dodania = serializers.DateField(auto_now=True)
    druzyna = serializers.PrimaryKeyRelatedField(queryset=Druzyna.objects.all())

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass