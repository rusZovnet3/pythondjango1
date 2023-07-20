from django.contrib import admin
from .models import Cursos,Categorias

# Register your models here.
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ("Nombre","Descripcion","Estado")     # interfaz de la tabla categoria
    search_fields = ('Nombre',)             # Filtrar la categoria por nombre ó descripcion
    list_filter = ('Nombre','Estado')
    
admin.site.register(Categorias,CategoriasAdmin)

# 
class CursosAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cursos,CursosAdmin)