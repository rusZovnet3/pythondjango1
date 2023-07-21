from django.db import models
from ..models import Cursos,    # .. salir de carpeta, acceder al archivo models.py


class Cursos_models():
    def cursos_list():
        cursos = Cursos.objects.order_by('Nombre')
        return cursos