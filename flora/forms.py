from django import forms

from .models import Zona
from .models import Especie


class FormularioZona(forms.ModelForm):
    class Meta:
        model = Zona
        fields = ('Nombre', 'Descripcion')

        labels = {
            'Nombre' :  'Ingrese nombre de la zona',
            'Descripcion' : 'Descripcion'
         }

class FormularioEspecie(forms.ModelForm):
    class Meta:
        model = Especie
        fields = ('Nombre', 'Nombre_Cientifico', 'Autor', 'Origen','Pais','Altura','Tipo', 'Estado', 'Luminosidad', 'Tolerancia_Frio', 'Humedad_Suelo',
                  'Hojas', 'Flores', 'Semillas', 'Imagen_Perfil', 'Imagen1','Imagen2', 'Imagen3', 'Zona', 'Localizacion')

        labels = {
            'Nombre' :  'Ingrese un nombre',
            'Nombre_Cientifico' : 'Ingrese su nombre cientifico',
            'Autor' : 'Ingrese el autor',
            'Origen' : 'Seleccione su origen',
            'Pais' : 'Ingrese un país',
            'Altura' : 'Ingrese la altura',
            'Tipo' : 'Seleccione el tipo de la especie',
            'Estado' : 'Seleccione su estado',
            'Luminosidad' : 'Seleccione la luminosidad',
            'Tolerancia_Frio' : 'Seleccione su tolerancia al frio',
            'Humedad_Suelo' : 'Seleccione su aguante a la humedad del suelo',
            'Hojas' : 'Ingrese la descripcion de las hojas',
            'Flores' : 'Ingrese la descripcion de las flores',
            'Semillas' : 'Ingrese la descripcion de las semillas',
            'Imagen_Perfil' : 'Ingrese imagen de perfil',
            'Imagen1' : 'Ingrese primera imagen',
            'Imagen2': 'Ingrese segunda imagen',
            'Imagen3': 'Ingrese tercera imagen',
            'Zona' : 'Seleccione su zona',
            'Localizacion' : 'ingrese URL de la localizacion'
         }
