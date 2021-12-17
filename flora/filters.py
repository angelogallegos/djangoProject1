import django_filters
from .models import Zona

class ZonaFilter(django_filters.FilterSet):

    class Meta:
        model = Zona
        fields = ('Nombre',)

