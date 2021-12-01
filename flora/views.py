from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView, ListView, CreateView, TemplateView
from django.urls import reverse_lazy

from flora.models import Zona
from flora.models import Especie
from flora.forms import FormularioZona
from flora.forms import FormularioEspecie


# Crud especie.
class RegistrarEspecie(CreateView):
    model = Especie
    template_name = 'agregar_especie.html'
    form_class = FormularioEspecie
    success_url = reverse_lazy('mostrar_especie')

class ListarEspecie(ListView):
    model = Especie
    template_name = 'mostrar_especie.html'
    queryset = Especie.objects.all()

class ModificarEspecie(UpdateView):
        model = Especie
        template_name = 'modificar_especie.html'
        form_class = FormularioEspecie
        success_url = reverse_lazy('mostrar_especie')

class EliminarEspecie(DeleteView):
        model = Especie
        template_name = 'confirmar_eliminacion_especie.html'
        success_url = reverse_lazy('mostrar_especie')

# Crud de zona
class RegistrarZona(CreateView):
    model = Zona
    template_name = 'agregar_zona.html'
    form_class = FormularioZona
    success_url = reverse_lazy('mostrar_zona')

class ListarZona(ListView):
    model = Zona
    template_name = 'mostrar_zona.html'
    queryset = Zona.objects.all()

class ModificarZona(UpdateView):
    model = Zona
    template_name = 'modificar_zona.html'
    form_class = FormularioZona
    success_url = reverse_lazy('mostrar_zona')

class EliminarZona(DeleteView):
    model = Zona
    template_name = 'confirmar_elimminacion.html'
    success_url = reverse_lazy('mostrar_zona')
