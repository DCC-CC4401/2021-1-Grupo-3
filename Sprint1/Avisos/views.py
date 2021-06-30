from django.shortcuts import render
from django.contrib.auth.models import User
from Avisos.models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


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
            foto = request.FILES['foto-mascota']
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

def avisos_adopcion(request):
    if request.user.is_authenticated:
        todos_adopcion= Adopcion.objects.order_by('-Fecha')
        mis_avisos_adopcion= Adopcion.objects.filter(Nombre_De_Usuario=request.user).order_by('-Fecha')
        if request.method == 'GET':
            return render(request,"avisos_adopcion.html", {'todos_adopcion': todos_adopcion, 
            'mis_avisos_adopcion':mis_avisos_adopcion})
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
            foto = request.FILES['foto-mascota']
            caracteristicas = request.POST['caracteristicas']
            edad = request.POST['edad']
            comentario = request.POST['comentarios']
            numero = request.POST['numero']
            adopcion = Adopcion.objects.create(Comuna=comuna, Region=region, Tipo_Animal=Tipo_Animal, Sexo=sexo,
            Nombre_De_Usuario=request.user, Caracteristicas=caracteristicas, Comentarios=comentario, Foto=foto,
            Numero_Telefonico=numero, Edad=edad)
        return HttpResponseRedirect('/inicio')
    else:
        return HttpResponseRedirect('/register_user')

def mp_remove(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Aviso, pk=pk)
        if request.user==post.Nombre_De_Usuario:
            post.delete()
    return redirect('mascotas_perdidas')

def adopcion_remove(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Adopcion, pk=pk)
        if request.user==post.Nombre_De_Usuario:
            post.delete()
    return redirect('avisos_adopcion')

def aviso_adopcion_en_detalle(request):
    if request.user.is_authenticated:
        id=request.GET["id"]
        aviso_en_detalle= Adopcion.objects.filter(Id=id)
        nombre= aviso_en_detalle[0].Nombre_De_Usuario
        usuario= User.objects.filter(username=nombre)
        email= usuario[0].email
        print(email)
        return render(request,"aviso_adopcion_en_detalle.html",{'aviso_en_detalle': aviso_en_detalle ,
        'email': email})
    else:
        return HttpResponseRedirect('/register_user')
