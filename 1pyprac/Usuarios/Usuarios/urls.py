"""Usuarios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

# invocando a la ruta del archivo, importando la funcion index
from App.Controllers.IndexController import IndexController
from App.Controllers.CursosController import CursosController
from App.Controllers.UserController import UserController
from App.Controllers.ProfileController import ProfileController

urlpatterns = [
    # Obtenemos los parametros que se ingresan a travez de la url para ejecutar las vistas segun el parametro
    #path('Llanque/<int:year>', IndexController.index, name='index'),
    path('', IndexController.index, name='index'),
    path('about', IndexController.about, name='about'),
    path('admin/', admin.site.urls, name='login'),
    path('cursos', CursosController.index, name='cursos'),
    path('details/<int:cursoid>/', CursosController.details, name='details'),  #dato GET
    path('obtener', CursosController.obtener_curso, name="obtener"),
    path('register', UserController.register, name="register"),
    path('mis_cursos', CursosController.mis_cursos, name='mis_cursos'),
    path('profile', ProfileController.profile, name='profile'),
    path('updateImage', ProfileController.updateImage, name='updateImage'),
    path('updateUser', ProfileController.updateUser, name='updateUser'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
