from django.contrib import admin

from .models import Osoba
# Register your models here.

class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko']

admin.site.register(Osoba, OsobaAdmin)

