# Generated by Django 3.2 on 2021-06-21 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Avisos', '0011_auto_20210621_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adopcion',
            name='Fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 21, 12, 39, 51, 415357)),
        ),
        migrations.AlterField(
            model_name='aviso',
            name='Fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 21, 12, 39, 51, 415357)),
        ),
    ]
