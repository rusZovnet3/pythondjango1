from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from App.Models.Profile_forms import ImageForm
from App.Models.Profile_models import Profile_models
from django.contrib.auth.models import User

class ProfileController():
    
    @login_required   # metodo en la que esta iniciado sesion el usuario a los procedimientos
    
    def profile(request):
        userid  = request.user.id   # id del login sesionado
        user    = User.objects.get(id=userid)  # compara la id con la DB de la tabla User
        profile = Profile_models.getProfile(userid)
        
        context = {
            'imageForm': ImageForm(),
            'profile': profile,
        }
        return render(request, 'views/profile/profile.html', context)
    
    @login_required
    
    def updateImage(request):
        if request.method == "POST":  # Sí los datos estan cargado
            userid  = request.user.id  # la id del usuario logueado
            profile = Profile_models.getProfile(userid)
            form    = ImageForm(request.POST, request.FILES,instance=profile)
            
            if form.is_valid():
                form.user = userid
                form.save()
                profile   =  Profile_models.getProfile(userid)
                context = {
                   'imageForm':ImageForm() ,
                   'profile': profile,
               }
            else:
                context = {
                   'imageForm':ImageForm() ,
                   'profile': profile,
               }
        return render(request, 'views/profile/profile.html',context)