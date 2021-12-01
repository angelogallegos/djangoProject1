from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView, ListView, CreateView, TemplateView
from django.urls import reverse_lazy

from flora.models import Zona
from flora.models import Origen
from flora.forms import FormularioZona
from flora.forms import FormularioOrigen

# Create your views here.
def mostrar_especie(request):
    return render(request, 'mostrar_especie.html')

def agregar_especie(request):
    return render(request, 'agregar_especie.html')



def mostrar_tipo_especie(request):
    return render(request, 'mostrar_tipo_especie.html')

def mostrar_origen(request):
    return render(request, 'mostrar_origen.html')

def mostrar_zona(request):
    return render(request, 'mostrar_zona.html')

def agregar_tipo_especie(request):
    return render(request, 'agregar_tipo_especie.html')

def agregar_origen(request):
    return render(request, 'agregar_origen.html')

# Crud de origen
class RegistrarOrigen(CreateView):
    model = Origen
    template_name = 'agregar_origen.html'
    form_class = FormularioOrigen
    success_url = reverse_lazy('mostrar_origen')

class ListarOrigen(ListView):
        model = Origen
        template_name = 'mostrar_origen.html'
        queryset = Origen.objects.all()

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
