from django.contrib import admin
from .models import *

class boksAdmin(admin.ModelAdmin):
    list_display = (('id', 'panjang', 'lebar', 'tinggi', 'isi'))
admin.site.register(boks, boksAdmin)


