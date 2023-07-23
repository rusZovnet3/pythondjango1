from django.db import models
from ..models import Cursos


class Cursos_models():
    def cursos_list():
        # Ordenar por nombres
        cursos = Cursos.objects.order_by('Nombre')
        return cursos
    
    def getcurso(idcurso):
        curso = Cursos.objects.get(CursoId=idcurso)
        return curso