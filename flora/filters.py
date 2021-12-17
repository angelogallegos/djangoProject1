import django_filters
from .models import Zona
from .models import Especie

class ZonaFilter(django_filters.FilterSet):

    class Meta:
        model = Zona
        fields = ('Nombre',)


class EspecieFilter(django_filters.FilterSet):

    class Meta:
        model = Especie
        fields = ('Nombre','Nombre_Cientifico','Tipo','Estado','Tolerancia_Frio', 'Humedad_Suelo','Luminosidad')