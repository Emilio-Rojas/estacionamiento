# Generated by Django 3.2.3 on 2021-06-12 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0005_auto_20210612_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloquedisponibilidad',
            name='disponibilidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bloque_disponibilidad', to='estacionamientos.disponibilidad'),
        ),
    ]
