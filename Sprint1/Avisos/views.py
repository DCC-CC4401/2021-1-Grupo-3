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
    last = Aviso.objects.order_by('-Fecha')[:6]
    if request.user.is_authenticated:
        if request.method == 'GET':
             return render(request,"Inicio.html",{'last':last})
        if request.method == 'POST':
            region = request.POST['region']
            comuna = request.POST['comuna']
            Tipo_Animal = request.POST['tipo-mascota']
            sexo = request.POST['sexo-mascota']
            foto = request.POST['foto-mascota']
            motivo = request.POST['tipo-pub']
            titulo = request.POST['title']
            comentario = request.POST['comentarios']
            aviso = Aviso.objects.create(Motivo=motivo, Titulo=titulo,Comuna=comuna, Region=region, Tipo_Animal=Tipo_Animal,
            Sexo=sexo, Nombre_De_Usuario=request.user, Descripcion=comentario, Foto=foto)
        return HttpResponseRedirect('/inicio')
    else:
        if request.method == 'GET':
             return render(request,"Inicio.html",{'last':last})
        if request.method == 'POST':
            username = request.POST['nombre_usuario']
            contraseña = request.POST['contraseña']
            usuario = authenticate(username=username,password=contraseña)
            if usuario is not None:
                login(request,usuario)
                return render(request,"Inicio.html", {'last': last})
            else:
                return HttpResponseRedirect('/register_user')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/inicio')

def avisos_mascotas_perdidas(request):
    todos = Aviso.objects.order_by('-Fecha')
    

    if request.user.is_authenticated:
        mis_avisos= Aviso.objects.filter(Nombre_De_Usuario=request.user)
        if request.method == 'GET':
             return render(request,"avisos_mascotas_perdidas.html", {'todos': todos, 'mis_avisos': mis_avisos})
    else:
        if request.method == 'GET':
             return render(request,"avisos_mascotas_perdidas.html", {'todos': todos})
        if request.method == 'POST':
            username = request.POST['nombre_usuario']
            contraseña = request.POST['contraseña']
            usuario = authenticate(username=username,password=contraseña)
            if usuario is not None:
                login(request,usuario)
                return render(request,"avisos_mascotas_perdidas.html", {'todos': todos})
            else:
                return HttpResponseRedirect('/register_user')


def adoption_form(request):
    if request.user.is_authenticated:
        if request.method == 'GET': #si estamos accediendo a la página
            return render(request,"adoption_form.html")
        if request.method == 'POST':
            region = request.POST['region']
            comuna = request.POST['comuna']
            Tipo_Animal = request.POST['tipo-mascota']
            sexo = request.POST['sexo-mascota']
            foto = request.POST['foto-mascota']
            caracteristicas = request.POST.get('caracteristicas', ' ')
            edad = request.POST['edad']
            comentario = request.POST.get('comentarios', ' ')
            numero = request.POST.get('numero', ' ')
            adopcion = Adopcion.objects.create(Comuna=comuna, Region=region, Tipo_Animal=Tipo_Animal, Sexo=sexo,
            Nombre_De_Usuario=request.user, Caracteristicas=caracteristicas, Comentarios=comentario, Foto=foto,
            Numero_Telefonico=numero, Edad=edad)
        return HttpResponseRedirect('/inicio')
    else:
        return HttpResponseRedirect('/register_user')



