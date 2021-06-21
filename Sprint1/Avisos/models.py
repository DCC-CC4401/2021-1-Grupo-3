from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Fecha_De_Nacimiento = models.DateField()

class Aviso(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Motivo = models.CharField(max_length=15)
    Titulo = models.CharField(max_length=30)
    Comuna = models.CharField(max_length=30)
    Region = models.CharField(max_length=30)
    Fecha = models.DateTimeField(default=datetime.now())
    Tipo_Animal = models.CharField(max_length=40)
    Sexo = models.CharField(max_length=15)
    Nombre_De_Usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    Descripcion = models.CharField(max_length=250)
    Foto = models.ImageField(upload_to="images/")
    Estado_del_Aviso = models.BooleanField(default=False)

class Adopcion(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Comuna = models.CharField(max_length=30)
    Region = models.CharField(max_length=30)
    Fecha = models.DateTimeField(default=datetime.now())
    Tipo_Animal = models.CharField(max_length=40)
    Sexo = models.CharField(max_length=15)
    Comentarios = models.CharField(max_length=250)
    Foto = models.ImageField(upload_to="images/")
    Numero_Telefonico = models.IntegerField(max_length=8)
    Usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    Estado_del_Aviso = models.BooleanField(default=False)