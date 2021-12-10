from django.db import models
from boks.models import *

class rack(models.Model):
    id =models.AutoField(primary_key=True)
    input_buffer =models.IntegerField()
    output_buffer = models.IntegerField()
    cell = models.IntegerField()

class input_buffer(models.Model):
    id = models.AutoField(primary_key=True)
    no_rack =models.ForeignKey('rack',on_delete=models.CASCADE, related_name="+",to_field='id')
    no_input_buffer =models.IntegerField()
    datetime_pengisian =models.DateTimeField
    status_dipesan_cell =models.IntegerField
    isi_pesanan =models.ForeignKey('boks.boks',on_delete=models.CASCADE, related_name="+",to_field='id')

class cell(models.Model):
    id = models.AutoField(primary_key=True)
    datetime_pengisian = models.DateTimeField
    panjang = models.FloatField()
    lebar = models.FloatField()
    tinggi = models.FloatField()
    posisi_cell_x =models.FloatField()
    posisi_cell_y = models.FloatField()
    status_isi = models.ForeignKey('input_buffer',on_delete=models.CASCADE, related_name="+",to_field='id')
    status_dipesan_output_buffer =models.IntegerField()

class output_buffer(models.Model):
    id = models.AutoField(primary_key=True)
    no_rack =models.ForeignKey('rack',on_delete=models.CASCADE, related_name="+",to_field='id')
    no_output_buffer =models.IntegerField()
    boks = models.ForeignKey('cell',on_delete=models.CASCADE, related_name="+",to_field='id')
    status_dipesan_agv =models.IntegerField()

