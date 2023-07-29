from django import forms
from ..models import Profile

class ImageForm(forms.ModelForm):
    # atributos de formulario
    class Meta:
        model   = Profile
        fields  = ['image']