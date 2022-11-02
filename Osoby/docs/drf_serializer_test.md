from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Druzyna
from Druzyna.models import Druzyna
from Osoby.serializers import DruzynaSerializer
druzyna = Druzyna(nazwa='G2', kraj='ES')
druzyna.save()

serializerDruzyna = DruzynaSerializer(druzyna) 
serializerDruzyna.data

druzynaContent = JSONRenderer().render(serializerDruzyna.data)
druzynaContent

import io

stream = io.BytesIO(druzynaContent)
data = JSONParser().parse(stream)

deserializer = DruzynaSerializer(data=data)

deserializer.is_valid()
deserializer.errors
deserializer.fields
deserializer.validated_data
deserializer.save()
deserializer.data

# Osoby
from Osoby.models import Osoba
from Osoby.serializers import OsobaSerializer

osoba = Osoba(imie='Adam', nazwisko='Mickiewicz', data_dodania='2022-10-27', druzyna=druzyna)

osoba.save()

serializerOsoba = OsobaSerializer(osoba)   
serializerOsoba.data

OsobaContent = JSONRenderer().render(serializerOsoba.data)
OsobaContent

import io

stream = io.BytesIO(OsobaContent)
data = JSONParser().parse(stream)

deserializer = OsobaSerializer(data=data)

deserializer.is_valid()
deserializer.errors
deserializer.fields
deserializer.validated_data
deserializer.save()
deserializer.data
