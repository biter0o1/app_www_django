from rest_framework import serializers
from .models import Osoba, Druzyna, MIESIACE
from datetime import date


class OsobaSerializer(serializers.Serializer):
    # letters = RegexValidator(r'[a-zA-Z]+', 'Only alphanumeric characters are allowed.')

    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True)
    nazwisko = serializers.CharField(required=True)
    miesiac_urodzenia = serializers.ChoiceField(choices=MIESIACE, default=MIESIACE)
    data_dodania = serializers.DateField()
    druzyna = serializers.PrimaryKeyRelatedField(queryset=Druzyna.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    def validate(self, data):
        if not data['imie'].isalpha():
            raise serializers.ValidationError("Imie moze zawierac tylko litery")
        if data['data_dodania'] > date.today():
            raise serializers.ValidationError("Data nie może być wyższa niż dzisiejsza")
        return data

    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.miesiac_urodzenia = validated_data.get('miesiac_urodzenia', instance.miesiac_urodzenia)
        instance.data_dodania = validated_data.get('data_dodania', instance.data_dodania)
        instance.druzyna = validated_data.get('druzyna', instance.druzyna)
        instance.save()
        return instance



class DruzynaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nazwa = serializers.CharField(required=True)
    kraj = serializers.CharField(required=True)

    def create(self, validated_data):
        return Druzyna.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.kraj = validated_data.get('kraj', instance.kraj)
        instance.save()
        return instance


class OsobaModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Osoba
