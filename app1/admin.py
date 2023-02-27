from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Beruf)
admin.site.register(Lernfeldnr)
admin.site.register(Ausbildungsjahr)
admin.site.register(Vorlage)
admin.site.register(Lernfeld)
@admin.register(Inhalt)
class InhaltAdmin(admin.ModelAdmin):
    list_filter = ['lernfeld', 'lernfeld__beruf']
