from django import forms

from .models import Zona
from .models import Origen

class FormularioZona(forms.ModelForm):
    class Meta:
        model = Zona
        fields = ('Nombre', 'Descripcion')

        labels = {
            'Nombre' :  'Ingrese nombre de la zona',
            'Descripcion' : 'Descripcion'
         }

class FormularioOrigen(forms.ModelForm):
    class Meta:
        model = Origen
        fields = ('Nombre', 'Pais')

        labels = {
            'Nombre' :  'Ingrese un nombre',
            'Pais' : 'Ingrese el pais de origen'
         }