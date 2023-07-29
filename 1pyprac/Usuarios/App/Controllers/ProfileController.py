from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from App.Models.Profile_forms import ImageForm

class ProfileController():
    
    @login_required   # metodo en la que esta iniciado sesion el usuario a los procedimientos
    
    def profile(request):
        context = {
            'imageForm': ImageForm()
        }
        return render(request, 'views/profile/profile.html', context)