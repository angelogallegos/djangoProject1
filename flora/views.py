from fileinput import filename
from urllib import request
import os
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from django.http import HttpResponse
from django_filters import rest_framework as filters
from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView, ListView, CreateView, TemplateView, View
from django.urls import reverse_lazy
import io
from django.http import FileResponse
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import TableStyle, Table
from django.shortcuts import render

import flora
from flora.models import Zona
from flora.models import Especie
from flora.forms import FormularioZona
from flora.forms import FormularioEspecie
from .filters import ZonaFilter
from .filters import EspecieFilter


from django.contrib.auth.decorators import login_required
#qr pagina



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


# Zona de los json
import json
import socket


#ip = socket.gethostbyname(socket.gethostname()) + ':8000'
ip = '192.168.0.3:8000'

def buscar(request):
    especies = Especie.objects.all()
    especies = [especie_serializar(espe) for espe in especies]
    return HttpResponse(json.dumps(especies),content_type='application/json')

def especie_serializar(especie):
    uuid_str = str(especie.QR)
    return {'Nombre': especie.Nombre, 'Nombre_Cientifico': especie.Nombre_Cientifico, 'Autor': especie.Autor, 'Origen': especie.Origen.Nombre, 'Pais': especie.Pais, 'Altura': especie.Altura,  'Tipo': especie.Tipo.Nombre,  'Estado': especie.Estado.Nombre, 'Luminosidad': especie.Luminosidad.Nombre,'Tolerancia_Frio': especie.Tolerancia_Frio.Nombre, 'Humedad_Suelo': especie.Humedad_Suelo.Nombre, 'Hojas': especie.Hojas, 'Flores': especie.Flores, 'Semillas': especie.Semillas, 'Imagen_Perfil': ip + especie.Imagen_Perfil.url, 'QR': uuid_str, 'Localizacion': especie.Localizacion}
 #return {'Nombre': especie.Nombre, 'Imagen_1': '192.168.1.26:8000'+ especie.Imagen_Perfil.url}




# Zona de los reportes
def generar_reporte_zona(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Reporte_Zona.pdf'

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    zonas = Zona.objects.all()

    x = 30
    y = 630
    documentTitle = 'Reporte de zonas'
    c.setTitle(documentTitle)
    image = './media/logo.jpg'

    #header
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30,750,'Universidad')

    c.setFont('Helvetica', 12)
    c.drawString(30, 735, 'de Concepci??n')

    c.drawInlineImage(image, 430, 750)
    c.setFont('Helvetica-Bold', 12)
    c.drawString(490, 750, 'UdeC')
    c.line(460,747, 560, 747)

    c.setFillColor(colors.darkgoldenrod)
    c.setFont('Helvetica-Bold', 18)
    c.drawString(230, 680, "Reporte de las Zonas")


    for z in zonas:
        c.setFillColor(colors.black)
        c.setFont('Helvetica', 9)
        c.drawString(x, y, z.Nombre + ' |:| ' + z.Descripcion)
        y -= 12



    #guardar pdf
    c.save()


    pdf = buffer.getvalue()
    response.write(pdf)
    return response

def generar_reporte_especie(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Reporte_especie.pdf'

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    especies = Especie.objects.all()

    x = 30
    y = 630
    documentTitle = 'Reporte de especies'
    c.setTitle(documentTitle)
    image = './media/logo.jpg'

    #header
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30,750,'Universidad')

    c.setFont('Helvetica', 12)
    c.drawString(30, 735, 'de Concepci??n')

    c.drawInlineImage(image, 430, 750)
    c.setFont('Helvetica-Bold', 12)
    c.drawString(490, 750, 'UdeC')
    c.line(460,747, 560, 747)

    c.setFillColor(colors.darkgoldenrod)
    c.setFont('Helvetica-Bold', 18)
    c.drawString(230, 680, "Reporte de las especies")


    for z in especies:
        c.setFillColor(colors.black)
        c.setFont('Helvetica', 9)
        c.drawString(x, y, z.Nombre + ' |:| ' + z.Nombre_Cientifico + ' |:| ' + z.Altura+ ' |:| ' + z.Hojas+ ' |:| ' + z.Flores+ ' |:| ' + z.Semillas)
        y -= 12



    #guardar pdf
    c.save()


    pdf = buffer.getvalue()
    response.write(pdf)
    return response