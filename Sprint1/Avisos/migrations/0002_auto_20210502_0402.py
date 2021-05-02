# Generated by Django 3.1.7 on 2021-05-02 08:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Avisos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aviso',
            name='Fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 4, 2, 14, 634340)),
        ),
        migrations.AlterField(
            model_name='aviso',
            name='Id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='aviso',
            name='Nombre_De_Usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
