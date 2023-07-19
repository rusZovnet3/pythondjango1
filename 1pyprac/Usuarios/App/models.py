from django.db import models

# Create your models here.
class Cursos(models.Model):
    CursoId     = models.AutoField(primary_key=True)
    Imagen      = models.ImageField(null=True, upload_to='images/curso')
    Nombre      = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=50)
    Horas       = models.IntegerField(default=0)
    Costo       = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Estado      = models.BooleanField()
    
    
class Categorias(models.Model):
    CategoriaID = models.AutoField(primary_key=True)
    Nombre      = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=50)
    Estado      = models.BooleanField()
    CursoId     = models.ForeignKey(Cursos, on_delete=models.CASCADE)