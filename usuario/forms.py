from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import Usuario


class FormularioUsuario(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('nombres', 'apellidos', 'email', 'username', 'password1', 'password2')

        labels = {
            'nombres' :  'Ingrese nombre de usuario'
         }

class FormularioLogin (forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput) #decir que es un campo de tipo contraseña

    class Meta:
        model= Usuario
        fields=('username','password')

    def clean(self):            #
        if self.is_valid():
            username=self.cleaned_data['username']
            password=self.cleaned_data['password']
            if not authenticate(username=username,password=password):
                raise forms.ValidationError("Usuario o contraseña Incorrectos")

