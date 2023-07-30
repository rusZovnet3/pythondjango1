from django import forms   # metodos para invocar
from ..models import Profile
from django.contrib.auth.models import User

class ImageForm(forms.ModelForm):
    # atributos de formulario
    class Meta:
        model   = Profile
        fields  = ['image']
        
# Formulario de usuarios - perfil        
class UserForm(forms.ModelForm):
    first_name      = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nombre'
    }))
    last_name       = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Apellido'
    }))
    username        = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Usuario'
    }))
    email           = forms.EmailField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    
    class Meta:
        model   = User
        fields  = ['first_name', 'last_name', 'username', 'email']