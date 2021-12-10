from django.db import models

class boks(models.Model):
    id =models.AutoField(primary_key=True)
    panjang =models.FloatField()
    lebar =models.FloatField()
    tinggi = models.FloatField()
    isi =models.CharField(max_length=255)
