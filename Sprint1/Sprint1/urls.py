"""Sprint1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Avisos.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register_user/', register_user, name='register_user'),
    path('inicio/', inicio, name='inicio'),
    path('logout/', logout_user, name='logout_user'),
    path('mascotas_perdidas/', avisos_mascotas_perdidas, name= 'mascotas_perdidas'),
    path('formulario_adopcion/', adoption_form, name='formulario_adopcion'),
    path('post/<pk>/mp_remove/', mp_remove, name='mp_remove'),
    path('post/<pk>/adopcion_remove/', adopcion_remove, name='adopcion_remove'),
    path('avisos_adopcion/', avisos_adopcion, name='avisos_adopcion'),
    path('aviso_adopcion_en_detalle', aviso_adopcion_en_detalle, name='aviso_adopcion_en_detalle')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
