from django.contrib import admin
from django.utils.html import format_html
from .models import Cursos,Categorias

# Register your models here.
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ("Nombre","Descripcion","Estado")     # interfaz de la tabla categoria
    search_fields = ('Nombre',)             # Filtrar la categoria por nombre ó descripcion
    list_filter = ('Nombre','Estado')
    
admin.site.register(Categorias,CategoriasAdmin)

# 
class CursosAdmin(admin.ModelAdmin):
    #añadir imagen html a la página de editar
    def image_tag(self, obj):
        return format_html('<img width="85" height="45" src="/media/{}" />'.format(obj.Imagen))
    image_tag.short_description = 'Imagen'
    readonly_fields = ['image_tag']
    raw_id_fields = ('CategoriaID',)
    list_display = ('image_tag','Nombre','Descripcion','Horas','Costo','Estado')
    search_fields = ('Nombre','Descripcion')   # filtrar busqueda del curso
    pass

admin.site.register(Cursos,CursosAdmin)