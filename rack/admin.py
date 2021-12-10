from django.contrib import admin
from .models import *

class rackAdmin (admin.ModelAdmin):
    list_display=(('id', 'input_buffer', 'output_buffer', 'cell'))
admin.site.register(rack, rackAdmin)

class input_bufferAdmin(admin.ModelAdmin):
    list_display=(('id', 'no_rack', 'no_input_buffer', 'datetime_pengisian', 'status_dipesan_cell', 'isi_pesanan'))
admin.site.register(input_buffer, input_bufferAdmin)

class cellAdmin (admin.ModelAdmin):
    list_display=(('id', 'datetime_pengisian', 'panjang', 'lebar', 'tinggi', 'posisi_cell_x', 'posisi_cell_y', 'status_isi', 'status_dipesan_output_buffer'))
admin.site.register(cell, cellAdmin)

class output_bufferAdmin(admin.ModelAdmin):
    list_display=(('id', 'no_rack', 'no_output_buffer', 'boks', 'status_dipesan_agv'))
admin.site.register(output_buffer, output_bufferAdmin)
