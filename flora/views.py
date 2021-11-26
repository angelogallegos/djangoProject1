from django.shortcuts import render

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

def agregar_zona(request):
    return render(request, 'agregar_zona.html')