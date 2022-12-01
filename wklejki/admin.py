from django.contrib import admin
from .models import Wklejki

# Register your models here.

# class PersonAdmin(admin.ModelAdmin):
#     list_display = ['imie', 'nazwisko', 'druzyna']
#     list_filter = ('druzyna',)
#
#
# admin.site.register(Osoba, PersonAdmin)
admin.site.register(Wklejki)
#
# TokenAdmin.raw_id_fields=['user']
