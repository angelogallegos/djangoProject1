from urllib import request

from django.http import HttpResponse
from django_filters import rest_framework as filters

from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView, ListView, CreateView, TemplateView
from django.urls import reverse_lazy
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from flora.models import Zona
from flora.models import Especie
from flora.forms import FormularioZona
from flora.forms import FormularioEspecie
from .filters import ZonaFilter
from .filters import EspecieFilter


from django.contrib.auth.decorators import login_required

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EspecieFilter(self.request.GET, queryset=self.get_queryset())
        return context

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ZonaFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ModificarZona(UpdateView):
    model = Zona
    template_name = 'modificar_zona.html'
    form_class = FormularioZona
    success_url = reverse_lazy('mostrar_zona')


class EliminarZona(DeleteView):
    model = Zona
    template_name = 'confirmar_elimminacion.html'
    success_url = reverse_lazy('mostrar_zona')

import json

def buscar(request):
    especies = Especie.objects.all()
    especies = [especie_serializar(espe) for espe in especies]
    return HttpResponse(json.dumps(especies),content_type='application/json')

def especie_serializar(especie):
    return {'Nombre': especie.Nombre, 'Imagen_1': especie.Imagen_Perfil.url}
 #return {'Nombre': especie.Nombre, 'Imagen_1': '192.168.1.26:8000'+ especie.Imagen_Perfil.url}


def generar_reporte(request):
     buffer = io.BytesIO()
     x = 100
     y = 750

     pz = canvas.Canvas(buffer)

     pz.drawString(250, 800, "Reporte De Zona")

     zonas = Zona.objects.all()

     for z in zonas:
         pz.drawString(x,y, z.Nombre +' | '+ z.Descripcion)
         y-=12

     pz.showPage()
     pz.save()

     buffer.seek(0)
     return FileResponse(buffer, as_attachment=True, filename='REPORTE.pdf')