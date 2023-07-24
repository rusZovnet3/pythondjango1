from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from App.Models.User_forms import SignUpForm

class UserController():
    
    def register(request):
        if request.method == "POST":
            form = SignUpForm(request.POST)  # cargado de todo el dato al formulario
            if form.is_valid():   # verificar sí los datos son requeridos
                username = form.cleaned_data.get('user')  # invoca a la funcion get
                #return HttpResponseRedirect("admin/")
                return HttpResponse('<h1>Jimena Claros</h1>%s' % username)
            else:
                context = {'form': form}   # sí hay errores, se mantiene los datos del formulario
                return render(request, 'views/user/register.html', context)
            pass
        else:
            context = {'form': SignUpForm()}
            return render(request, 'views/user/register.html', context)