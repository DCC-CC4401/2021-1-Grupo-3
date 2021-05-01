from django.shortcuts import render
from django.contrib.auth.models import User
from Avisos.models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout


# Create your views here.
def register_user(request):
    if request.method == 'GET': #si estamos accediendo a la página
        return render(request,"register_user.html")
    elif request.method == 'POST': #si estamos recibiendo el formulario
        nombre = request.POST['nombre']
        nombre_de_usuario = request.POST['nombre_usuario']
        contraseña = request.POST['contraseña']
        Fecha_De_Nacimiento= request.POST['fecha']
        mail = request.POST['email']
        user = User.objects.create_user(username=nombre_de_usuario, password=contraseña,email=mail, first_name=nombre)
        mi_usuario = Usuario.objects.create(user=user, Fecha_De_Nacimiento=Fecha_De_Nacimiento)
        return HttpResponseRedirect('/inicio')

def inicio(request):
    last = Aviso.objects.all()[:6]
    if request.user.is_authenticated:
        return render(request,"Inicio.html",{'last':last})
    else:
        if request.method == 'GET':
             return render(request,"Inicio.html",{'last':last})
        if request.method == 'POST':
            username = request.POST['nombre_usuario']
            contraseña = request.POST['contraseña']
            usuario = authenticate(username=username,password=contraseña)
            if usuario is not None:
                login(request,usuario)
                return render(request,"Inicio.html")
            else:
                return HttpResponseRedirect('/register_user')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/inicio')

def avisos_mascotas_perdidas(request):
    return render(request, "avisos_mascotas_perdidas.html")