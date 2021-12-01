from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView, ListView, CreateView, TemplateView
from django.urls import reverse_lazy

from flora.models import Zona
from flora.models import Especie
from flora.forms import FormularioZona
from flora.forms import FormularioEspecie


# Crud especie.
def mostrar_especie(request):
    return render(request, 'mostrar_especie.html')

def agregar_especie(request):
    return render(request, 'agregar_especie.html')

class RegistrarEspecie(CreateView):
    model = Especie
    template_name = 'agregar_especie.html'
    form_class = FormularioEspecie
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
