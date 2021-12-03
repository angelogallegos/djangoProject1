from django.views.generic import UpdateView, DeleteView, ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from usuario.models import Usuario
from usuario.forms import FormularioUsuario, FormularioLogin

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