from django.shortcuts import render

# Create your views here.
def listar_usuarios(request):
    return render(request, 'listar_usuarios.html')

def agregar_usuario(request):
    return render(request, 'agregar_usuario.html.html')