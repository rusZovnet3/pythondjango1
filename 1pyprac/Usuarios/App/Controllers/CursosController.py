from django.shortcuts import render,HttpResponse
from App.Models.Cursos_models import Cursos_models
from django.http import HttpResponseRedirect
from ..models import Inscripcion
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class CursosController():
    def index(request):
        filtrar = None
        if request.method == "POST":   # POST de la busqueda de cursos
            filtrar = request.POST.get('filtrar')  # name='filtrar'  de busqueda
            
        cursos_list =  Cursos_models.cursos_list(filtrar)
        
        paginator   = Paginator(cursos_list, 6)  # Paginador
        page = request.GET.get('page')     # variable GET del paginador url
        
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items= paginator.page(paginator.num_pages)
        
        context = {'cursos_list': items}
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
                #return HttpResponse('<h1>Rosmery Condori Toledo</h1>%s' % cursoid)
                return HttpResponseRedirect('mis_cursos')
            else:
                return HttpResponseRedirect('admin')

    def mis_cursos(request):
        filtrar = None
        if request.method == "POST":
            filtrar = request.POST.get('filtrar')  # name="filtrar" de la vista mis_cursos
        
        cursos_list = Cursos_models.mis_cursos_list(request, filtrar)
        paginator   = Paginator(cursos_list, 6)  # Paginador
        page = request.GET.get('page')     # variable GET del paginador url
        
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items= paginator.page(paginator.num_pages)
            
        context = {
            'items':items,
        }
            
        return render(request, "views/cursos/mis_cursos.html", context)