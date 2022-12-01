from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Wklejki, Kategorie


class WklejkiSerializer(serializers.ModelSerializer):
    kategoria = serializers.ChoiceField(source='get_kategoria_display', choices=Kategorie)
    wlasciciel_wklejki = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Wklejki
        fields = '__all__'
