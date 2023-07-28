from django.shortcuts import render,HttpResponse
from App.Models.Cursos_models import Cursos_models
from django.http import HttpResponseRedirect
from ..models import Inscripcion
from datetime import date

class CursosController():
    def index(request):
        cursos_list =  Cursos_models.cursos_list()
        context = {'cursos_list': cursos_list}
        return render(request, 'views/cursos/cursos.html',context)
    
    def details(request,cursoid):
        objects = Cursos_models.getcurso(cursoid)
        #context = {'curso': objects[0], 'categoria': objects[1]}
        context = {'curso': objects}
        return render(request, 'views/cursos/details.html',context)
    
    def obtener_curso(request):
        if request.method == 'POST':
            # control de usuario logueado
            if request.user.is_authenticated:
                
                cursoid = request.POST['cursoid']
                user    = request.user.id
                model   = Inscripcion(
                    CursoId         = cursoid,
                    EstudianteID    = user,
                    Fecha           = date.today()
                )
                model.save()
                return HttpResponse('<h1>Rosmery Condori Toledo</h1>%s' % cursoid)
            else:
                return HttpResponseRedirect('admin')
