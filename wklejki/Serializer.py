from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Wklejki, Kategorie


class WklejkiSerializer(serializers.ModelSerializer):
    #kategoria = serializers.ChoiceField(source='get_kategoria_display', choices=Kategorie)
    #wlasciciel_wklejki = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    wlasciciel_wklejki = serializers.ReadOnlyField(source='wlasciciel_wklejki.username')

    def update(self, instance, validated_data):
        instance.tytul = validated_data.get('tytul', instance.tytul)
        instance.tekst = validated_data.get('tekst', instance.tekst)
        instance.kategoria = validated_data.get('kategoria', instance.kategoria)
        instance.save()
        return instance
    class Meta:
        model = Wklejki
        fields = '__all__'



