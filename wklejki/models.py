from django.db import models
from django.utils.translation import gettext_lazy as _


class Kategorie(models.IntegerChoices):
    zwykly_tekst = 1, _('Zwykły tekst')
    html = 2, _("HTML")
    css = 3, _("CSS")
    PHP = 4, _('PHP')
    Python = 5, _("PYTHON")
    Ruby = 6, _("Ruby")
    C = 7, _("C")
    Cpp = 8, _('C++')
    Go = 9, _('Go')
    Latex = 10, _('Latex')


class Wklejki(models.Model):
    tytul = models.CharField(max_length=255, blank=False)
    kategoria = models.IntegerField(choices=Kategorie.choices)
    wlasciciel_wklejki = models.ForeignKey('auth.User', null=True, on_delete=models.CASCADE)
    tekst = models.TextField(max_length=2137, blank=True, null=True)
    lajki = models.IntegerField(default=0)


    class Meta:
        indexes = [
            models.Index(fields=['kategoria'], name='kategoria_index'), # Index tylko dla wlasnych testow
        ]
        db_table = 'wklejki'
        verbose_name = 'Wklejki'
        verbose_name_plural = 'Wklejki'

    def __str__(self):
        return (self.tytul)