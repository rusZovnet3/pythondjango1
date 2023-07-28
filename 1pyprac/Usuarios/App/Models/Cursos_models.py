from django.db import models
from ..models import Cursos,Categorias,Inscripcion


class Cursos_models():
    def cursos_list():
        # Ordenar por nombres
        cursos = Cursos.objects.order_by('Nombre')
        return cursos
    
    def getcurso(idcurso):
        # coleccion de objetos
        '''curso = Cursos.objects.filter(CursoId=idcurso)
        for item in curso:
           categoria = Categorias.objects.get(CategoriaID=item.CategoriaID.CategoriaID)
        return [item,categoria]'''
        curso = Cursos.objects.get(CursoId=idcurso)
        return curso
    
    def mis_cursos_list(request):
        i           = 0
        inscripcion = Inscripcion.objects.filter(EstudianteID=request.user.id)
        curso       = [[]] * len(inscripcion)
        for item in inscripcion:
            curso[i]   = Cursos.objects.get(CursoId=item.CursoId)
            i += 1
        return curso