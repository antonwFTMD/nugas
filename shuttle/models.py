from django.db import models
from rack.models import *

class shuttle_input_buffer(models.Model):
    id = models.AutoField(primary_key=True)
    kecepatan_maks =models.FloatField()
    waktu_loading =models.FloatField()
    waktu_unloading = models.FloatField()
    input_buffer_to_cell =models.ForeignKey('rack.input_buffer',on_delete=models.CASCADE, related_name="+",to_field='id')
    shuttle_input_to_cell_x = models.ForeignKey('rack.cell', on_delete=models.CASCADE, related_name="+",to_field='id')
    shuttle_input_to_cell_y = models.ForeignKey('rack.cell', on_delete=models.CASCADE, related_name="+", to_field='id')

class shuttle_output_buffer(models.Model):
    id = models.AutoField(primary_key=True)
    kecepatan_maks =models.FloatField()
    waktu_loading =models.FloatField()
    waktu_unloading = models.FloatField()
    cell_to_output_buffer =models.ForeignKey('rack.output_buffer',on_delete=models.CASCADE, related_name="+",to_field='id')
    shuttle_to_output_x = models.ForeignKey('rack.cell', on_delete=models.CASCADE, related_name="+",to_field='id')
    shuttle_to_output_y = models.ForeignKey('rack.cell', on_delete=models.CASCADE, related_name="+",to_field='id')

