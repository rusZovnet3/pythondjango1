from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from App.Models.Profile_forms import ImageForm
from App.Models.Profile_models import Profile_models

class ProfileController():
    
    @login_required   # metodo en la que esta iniciado sesion el usuario a los procedimientos
    
    def profile(request):
        context = {
            'imageForm': ImageForm()
        }
        return render(request, 'views/profile/profile.html', context)
    
    @login_required
    
    def updateImage(request):
        if request.method == "POST":  # Sí los datos estan cargado
            userid  = request.user.id  # la id del usuario logueado
            p       = Profile_models.getProfile(userid)
            form    = ImageForm(request.POST, request.FILES,instance=p)
            if form.is_valid():
                form.user = userid
                form.save()
                p   =  Profile_models.getProfile(userid)
                context = {
                   'imageForm':ImageForm() ,
                   "user":p
               }
        return render(request, 'views/profile/profile.html',context)