# Generated by Django 5.0.6 on 2024-05-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='dni',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
