import django_filters
from .models import Usuario

class UsuarioFilter(django_filters.FilterSet):

    class Meta:
        model = Usuario
        fields = ('nombres','apellidos')