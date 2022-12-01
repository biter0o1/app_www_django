from django.contrib import admin
from .models import Wklejki

# Register your models here.

class WklejkiAdmin(admin.ModelAdmin):
    list_display = ['tytul', 'kategoria', 'wlasciciel_wklejki', 'tekst', 'lajki']
    list_filter = ('kategoria',)

admin.site.register(Wklejki, WklejkiAdmin)
