from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Wklejki, Kategorie


class WklejkiSerializer(serializers.ModelSerializer):
    #kategoria = serializers.ChoiceField(source='get_kategoria_display', choices=Kategorie)
    #wlasciciel_wklejki = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    wlasciciel_wklejki = serializers.ReadOnlyField(source='wlasciciel_wklejki.username')
    class Meta:
        model = Wklejki
        fields = '__all__'




#anonimowy uzytknownik moze zrobic wklejke za "kogos"
#auto uzupellnianie sie uzytkownika na anonimowy(brak)/istniejeacy,
# lajki deafultowo na 0 sa ale mozna dac im przy tworzeniu 100 lajkow - do poprawy ?
#przy aktualizacji nie powinno sie aktualizowac lajkow/uzytkownika (wyswietl mniej rzeczy)