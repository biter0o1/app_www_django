from django.db import models
from django.utils.translation import gettext_lazy as _


class Kategorie(models.TextChoices):
    zwykly_tekst = "ZWYKLY TEKST", _('ZWYKLY TEKST')
    html = "HTML", _("HTML")
    css = "CSS", _("CSS")
    PHP = "PHP", _('PHP')
    Python = "PYTHON", _("PYTHON")
    Ruby = "RUBY", _("RUBY")
    C = "C", _("C")
    Cpp = "C++", _('C++')
    Go = "GO", _('GO')
    Latex = "LATEX", _('LATEX')


class Wklejki(models.Model):
    tytul = models.CharField(max_length=255, blank=False)

    kategoria = models.CharField(choices=Kategorie.choices, max_length=255)

    wlasciciel_wklejki = models.ForeignKey('auth.User', null=True,blank=True, on_delete=models.CASCADE)
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