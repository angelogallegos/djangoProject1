from django.shortcuts import render

# Create your views here.
def mostrar_especies(request):
    return render(request, 'mostrar_especie.html')



def agregar_especies(request):
    return render(request, 'agregar_especie.html')