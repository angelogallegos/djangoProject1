from django.http import HttpResponse
from django.views.generic import UpdateView, DeleteView, ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
import io
from usuario.models import Usuario
from usuario.forms import FormularioUsuario, FormularioLogin
from .filters import UsuarioFilter

# Create your views here.

class RegistrarUsuario(CreateView):
    model = Usuario
    template_name = 'agregar_usuario.html'
    form_class = FormularioUsuario
    success_url = reverse_lazy('listar_usuarios')

def desloguearce(request):
    logout(request)
    return redirect('login')

@login_required()
def index(request):
    return render(request, 'polls/starter.html')

def login_view(request):
    usuario = request.user
    if usuario.is_authenticated:
        return redirect('index')
    if request.POST:
        form = FormularioLogin(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            usuario = authenticate(username=username, password=password)

            if usuario:
                login(request, usuario)

                return redirect('index')
    else:
        form = FormularioLogin()

    context = {'form_login': form}
    return render(request, 'registration/login.html', context)

class ListarUsuario(ListView):
    model = Usuario
    template_name = 'listar_usuarios.html'
    queryset = Usuario.objects.filter(is_admin=False, is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = UsuarioFilter(self.request.GET, queryset=self.get_queryset())
        return context

class EliminarUsuario(DeleteView):
    model = Usuario
    template_name = 'confirmar_eliminacion_usuario.html'

    def post(self, request, pk, *args, **kwargs):
        object = Usuario.objects.get(id=pk)
        object.is_active = False
        object.save()
        return redirect('listar_usuarios')

class ModificarUsuario(UpdateView):
    model = Usuario
    template_name = 'modificar_usuario.html'
    form_class = FormularioUsuario
    success_url = reverse_lazy('listar_usuarios')


import json

def buscar(request):
    usuarios = Usuario.objects.all()
    usuarios = [usuario_serializar(user) for user in usuarios]
    return HttpResponse(json.dumps(usuarios),content_type='application/json')

def usuario_serializar(usuario):
    return {'Nombre': usuario.nombres, 'Apellido': usuario.apellidos, 'email': usuario.email, 'Usuario': usuario.username}

# Zona de los reportes
def generar_reporte_usuario(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Reporte_Usuarios.pdf'

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    usuarios = Usuario.objects.all()

    x = 30
    y = 630
    documentTitle = 'Reporte de Usuarios'
    c.setTitle(documentTitle)
    image = './media/logo.jpg'

    #header
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30,750,'Universidad')

    c.setFont('Helvetica', 12)
    c.drawString(30, 735, 'de Concepción')

    c.drawInlineImage(image, 430, 750)
    c.setFont('Helvetica-Bold', 12)
    c.drawString(490, 750, 'UdeC')
    c.line(460,747, 560, 747)

    c.setFillColor(colors.darkgoldenrod)
    c.setFont('Helvetica-Bold', 18)
    c.drawString(230, 680, "Reporte de las Zonas")


    for z in usuarios:
        c.setFillColor(colors.black)
        c.setFont('Helvetica', 9)
        c.drawString(x, y, z.nombres + ',' + z.apellidos + ' = ' + z.username)
        y -= 12



    #guardar pdf
    c.save()


    pdf = buffer.getvalue()
    response.write(pdf)
    return response