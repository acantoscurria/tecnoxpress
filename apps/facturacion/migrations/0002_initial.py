# Generated by Django 5.0.6 on 2024-05-13 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facturacion', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='carrito',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='productos.carrito'),
        ),
    ]
