# Generated by Django 3.2.9 on 2021-12-10 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='boks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('panjang', models.FloatField()),
                ('lebar', models.FloatField()),
                ('tinggi', models.FloatField()),
                ('isi', models.CharField(max_length=255)),
            ],
        ),
    ]
