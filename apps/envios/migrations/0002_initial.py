# Generated by Django 5.0.6 on 2024-05-13 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('envios', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='envio',
            name='carrito',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='productos.carrito'),
        ),
    ]
