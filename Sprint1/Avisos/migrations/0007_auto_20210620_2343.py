# Generated by Django 3.2 on 2021-06-21 03:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Avisos', '0006_auto_20210620_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adopcion',
            name='Fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 20, 23, 43, 43, 827019)),
        ),
        migrations.AlterField(
            model_name='aviso',
            name='Fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 20, 23, 43, 43, 827019)),
        ),
    ]