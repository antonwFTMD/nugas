from django.contrib import admin
from .models import *

class shuttle_input_bufferAdmin(admin.ModelAdmin):
    list_display = (('id', 'kecepatan_maks', 'waktu_loading', 'waktu_unloading', 'input_buffer_to_cell', 'shuttle_input_to_cell_x', 'shuttle_input_to_cell_y'))
admin.site.register(shuttle_input_buffer, shuttle_input_bufferAdmin)


class shuttle_output_bufferAdmin(admin.ModelAdmin):
    list_display = (('id', 'kecepatan_maks', 'waktu_loading', 'waktu_unloading', 'cell_to_output_buffer', 'shuttle_to_output_x', 'shuttle_to_output_y'))
admin.site.register(shuttle_output_buffer, shuttle_output_bufferAdmin)
