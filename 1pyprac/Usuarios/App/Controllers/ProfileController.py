from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from App.Models.Profile_forms import ImageForm,UserForm,ProfileForm,DateForm,PasswordForm
from App.Models.Profile_models import Profile_models
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

class ProfileController():
    
    @login_required   # metodo en la que esta iniciado sesion el usuario a los procedimientos
    def profile(request):
        userid  = request.user.id   # id del login sesionado
        user    = User.objects.get(id=userid)  # compara la id con la DB de la tabla User
        profile = Profile_models.getProfile(userid)
        
        context = {
            'imageForm': ImageForm(),  # atributos de form y datos de la tabla profile
            'form1': UserForm(),    # el formulario de usuario
            'form2': ProfileForm(),  #  form de perfil con atributo especifico
            'dateForm': DateForm(),   # form campo fecha de la tabla profile
            'profile': profile,
            'user': user,
            'password': PasswordForm(),  # form campo password de la tabla User
        }
        return render(request, 'views/profile/profile.html', context)
    
    
    @login_required
    def updateImage(request):
        if request.method == "POST":  # Sí los datos estan cargado
            userid  = request.user.id  # la id del usuario logueado
            profile = Profile_models.getProfile(userid)
            user    = User.objects.get(id=userid)  # compara la id con la DB de la tabla User
            form    = ImageForm(request.POST, request.FILES,instance=profile)
            
            if form.is_valid():
                form.user = userid
                form.save()
                profile   =  Profile_models.getProfile(userid)
                context = {
                   'imageForm':ImageForm(),
                   'form1': UserForm(),  # el formulario de usuario
                   'form2': ProfileForm(),  #  form de perfil con atributo especifico
                   'dateForm': DateForm(),   # form campo fecha de la tabla profile
                   'profile': profile,
                   'user': user,
                   'password': PasswordForm(),  # form campo password de la tabla User
               }
            else:
                context = {
                   'imageForm':ImageForm(),
                   'form1': UserForm(),   # el formulario de usuario
                   'form2': ProfileForm(),  #  form de perfil con atributo especifico
                   'dateForm': DateForm(),   # form campo fecha de la tabla profile
                   'profile': profile,
                   'user': user,
                   'password': PasswordForm(),  # form campo password de la tabla User
               }
        return render(request, 'views/profile/profile.html',context)
    
    
    @login_required
    def updateUser(request):
        # verificar sí estan cargado los datos del form usuario
        if request.method == "POST":
            # id del usuario logueado
            userid  = request.user.id
            # buscar la id logueado a la DB de usuario
            user    = User.objects.get(id=userid)
            
            profile = Profile_models.getProfile(userid)
            
            # extraer todo las POST, resultado de busqueda desde la DB del usuario logueado
            form1   = UserForm(request.POST, instance=user)
            form2   = ProfileForm(request.POST, instance=profile)
            form3   = DateForm(request.POST, instance=profile)   # form , metodo campo fecha
            
            if form1.is_valid() and form2.is_valid() and form3.is_valid():
                form1.save()
                form2.save()
                form3.save()
                profile = Profile_models.getProfile(userid)
                context = {
                   'imageForm':ImageForm(),
                   'form1': UserForm(),  # el formulario de usuario
                   'form2': ProfileForm(),  #  form de perfil con atributo especifico
                   'dateForm': DateForm(),   # form campo fecha de la tabla profile
                   'profile': profile,
                   'user': user,
                   'password': PasswordForm(),  # form campo password de la tabla User
               }
                
        return render(request, 'views/profile/profile.html',context)
    
    
    @login_required
    def updatePassword(request):
        userid      = request.user.id
        user        = User.objects.get(id=userid)  # mostrar por id en la DB del id logueado
        form1       = PasswordForm(request.POST, instance=user)
        
        if request.method == "POST" and form1.is_valid():
            user.set_password(form1.cleaned_data['password'])  # la fila buscada, se carga el password en el campo de password
            form1.save()
        return HttpResponseRedirect("admin/")
    