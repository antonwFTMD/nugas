# Generated by Django 3.2.9 on 2021-12-10 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cell',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('panjang', models.FloatField()),
                ('lebar', models.FloatField()),
                ('tinggi', models.FloatField()),
                ('posisi_cell_x', models.FloatField()),
                ('posisi_cell_y', models.FloatField()),
                ('status_dipesan_output_buffer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='rack',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('input_buffer', models.IntegerField()),
                ('output_buffer', models.IntegerField()),
                ('cell', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='output_buffer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('no_output_buffer', models.IntegerField()),
                ('status_dipesan_agv', models.IntegerField()),
                ('boks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rack.cell')),
                ('no_rack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rack.rack')),
            ],
        ),
        migrations.CreateModel(
            name='input_buffer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('no_input_buffer', models.IntegerField()),
                ('isi_pesanan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='boks.boks')),
                ('no_rack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rack.rack')),
            ],
        ),
        migrations.AddField(
            model_name='cell',
            name='status_isi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rack.input_buffer'),
        ),
    ]
