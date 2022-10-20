from django.contrib import admin

from .models import Druzyna
# Register your models here.
class DruzynaAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'kraj']

admin.site.register(Druzyna, DruzynaAdmin)