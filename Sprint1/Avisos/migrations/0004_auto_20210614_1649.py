# Generated by Django 3.1.7 on 2021-06-14 20:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Avisos', '0003_auto_20210502_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aviso',
            name='Fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 14, 16, 49, 17, 778464)),
        ),
        migrations.CreateModel(
            name='Adopcion',
            fields=[
                ('Id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Comuna', models.CharField(max_length=30)),
                ('Region', models.CharField(max_length=30)),
                ('Fecha', models.DateTimeField(default=datetime.datetime(2021, 6, 14, 16, 49, 17, 779463))),
                ('Tipo_Animal', models.CharField(max_length=40)),
                ('Sexo', models.CharField(max_length=15)),
                ('Caracteristicas', models.CharField(max_length=250)),
                ('Comentarios', models.CharField(max_length=250)),
                ('Foto', models.ImageField(upload_to='images/')),
                ('Estado_del_Aviso', models.BooleanField(default=False)),
                ('Numero_Telefonico', models.CharField(max_length=8)),
                ('Nombre_De_Usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
