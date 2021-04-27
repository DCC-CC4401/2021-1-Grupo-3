from django.db import models

# Create your models here.
class Usuario(models.Model):
    Nombre = models.CharField(max_length=30)
    Nombre_De_Usuario = models.CharField(max_length=30)
    Fecha_De_Nacimiento = models.DateField()
    Email = models.EmailField()
    Contraseña = models.CharField(max_length=15)

class Aviso(models.Model):
    Id = models.IntegerField()
    Motivo = models.CharField(max_length=15)
    Titulo = models.CharField(max_length=30)
    Comuna = models.CharField(max_length=30)
    Fecha = models.DateTimeField()
    Tipo_Animal = models.CharField(max_length=30)
    Sexo = models.CharField(max_length=15)
    Nombre_De_Usuario = models.ForeignKey(Usuario)
    Descripcion = models.CharField(max_length=250)
    Foto = models.ImageField()
    Estado_del_Aviso = models.BooleanField()