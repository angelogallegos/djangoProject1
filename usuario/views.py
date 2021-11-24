from django.shortcuts import render

# Create your views here.
def listar_usuarios(request):
    return render(request, 'listar_usuarios.html')