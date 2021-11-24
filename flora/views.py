from django.shortcuts import render

# Create your views here.
def mostrar_especies(request):
    return render(request, 'mostrar_flora.html')



def agregar_especies(request):
    return render(request, 'agregar_especie.html')