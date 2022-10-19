from django.db import models

from django.utils.translation import gettext_lazy as _

class Osoba(models.Model):
    class Miesiace(models.IntegerChoices):
        STYCZEN = 1, _('Styczeń')
        LUTY = 2, _('Luty')
        MARZEC = 3, _('Marzec')
        KWIECIEN = 4, _('Kwiecień')
        MAJ = 5, _('Maj')
        CZERWIEC = 6, _('Czerwiec')
        LIPIEC = 7, _('Lipiec')
        SIERPIEN = 8, _('Sierpień')
        WRZESIEN = 9, _('Wrzesień')
        PAZDZIERNIK = 10, _('Październik')
        LISTOPAD = 11, _('Listopad')
        GRUDZIEN = 12, _('Grudzień')

    imie = models.CharField(max_length=30, blank=False)
    nazwisko = models.CharField(max_length=30, blank=False)
    miesiac_urodzenia = models.IntegerField(max_length=2, choices=Miesiace.choices, default=Miesiace.CZERWIEC)
    data_dodania = models.DateField(auto_now=True)
