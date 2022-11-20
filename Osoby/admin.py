from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from .models import Osoba
# Register your models here.

class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'miesiac_urodzenia', 'data_dodania', 'druzyna']
    list_filter = ('druzyna', 'data_dodania')

admin.site.register(Osoba, OsobaAdmin)

TokenAdmin.raw_id_fields = ['user']