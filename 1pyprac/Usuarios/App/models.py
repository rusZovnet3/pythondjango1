from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings

# Create your models here.

class Categorias(models.Model):
    CategoriaID = models.AutoField(primary_key=True)
    Nombre      = models.CharField(max_length=50)
    Descripcion = models.TextField()
    Estado      = models.BooleanField()
    
class Cursos(models.Model):
    CursoId     = models.AutoField(primary_key=True)
    Imagen      = models.ImageField(null=True, upload_to='images/curso')
    Nombre      = models.CharField(max_length=50)
    Descripcion = models.TextField()
    Horas       = models.IntegerField(default=0)
    Costo       = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Estado      = models.BooleanField()
    CategoriaID = models.ForeignKey(Categorias, blank=True, null=True, on_delete=models.CASCADE)
    
class Inscripcion(models.Model):
    CursoId         = models.IntegerField(default=0)
    EstudianteID    = models.IntegerField(default=0)
    Fecha           = models.CharField(max_length=20)
    
class Profile(models.Model):
    
    def path_and_rename(path):
        
        def wrapper(instance, filename):
            
            ext = filename.split('.')[-1]
            filename = '{}.{}'.format(instance.pk, ext)
            archivo = os.path.join(settings.MEDIA_ROOT + "/" + path, filename)
            
            if os.path.isfile(archivo):   # sí ese archivo existe en la bd
               os.remove(archivo)     # remover
            return os.path.join(path, filename)
        
        return wrapper
            
    profileId       = models.AutoField(primary_key=True)
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    number_phone    = models.CharField(max_length=20)
    location        = models.CharField(max_length=50)
    birth_date      = models.DateField(null=True, blank=True)
    image           = models.ImageField(null=True,upload_to=path_and_rename('images/profile'))