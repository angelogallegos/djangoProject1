from django import forms

from .models import Zona

class FormularioZona(forms.ModelForm):
    class Meta:
        model = Zona
        fields = ('Nombre', 'Descripcion')

        labels = {
            'Nombre' :  'Ingrese nombre de la zona',
            'Descripcion' : 'Descripcion'
         }