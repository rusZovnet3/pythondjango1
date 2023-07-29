from django.contrib.auth.decorators import login_required
from django.shortcuts import render

class ProfileController():
    
    @login_required   # metodo en la que esta iniciado sesion el usuario a los procedimientos
    
    def profile(request):
        return render(request, 'views/profile/profile.html')