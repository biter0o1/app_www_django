from django.contrib import admin

from .models import Osoba
# Register your models here.

class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'miesiac_urodzenia', 'data_dodania', 'druzyna']
    list_filter = ('druzyna', 'data_dodania')

admin.site.register(Osoba, OsobaAdmin)

