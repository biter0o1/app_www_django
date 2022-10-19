from django.db import models

class Osoba(models.Model):
    miesiace = (
        ('1', 'Styczeń'),
        ('2', 'Luty'),
        ('3', 'Marzec'),
        ('4', 'Kwiecień'),
        ('5', 'Maj'),
        ('6', 'Czerwiec'),
        ('7', 'Lipiec'),
        ('8', 'Sierpień'),
        ('9', 'Wrzesień'),
        ('10', 'Październik'),
        ('11', 'Listopad'),
        ('12', 'Grudzień'),
    )

    imie = models.CharField(max_length=30, blank=False)
    nazwisko = models.CharField(max_length=30, blank=False)
    miesiac_urodzenia = models.CharField(max_length=30, choices=miesiace)
