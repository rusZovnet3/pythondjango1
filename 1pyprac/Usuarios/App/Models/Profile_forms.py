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
        
        
class ProfileForm(forms.ModelForm):
    number_phone    = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Telefono'
    }))
    location        = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Direccion'
    }))
    
    class Meta:
        model   = Profile   #  la tabla profile
        fields  = ['number_phone', 'location']
        
        
class DateForm(forms.ModelForm):
    birth_date = forms.DateTimeField(label='', 
        input_formats   = ['%d/%m/%Y'], 
        widget          = forms.DateTimeInput(attrs = {
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }))
    
    class Meta:
        model   = Profile   #  la tabla profile
        fields  = ['birth_date']