from django.urls import path
from flora import  views

urlpatterns = [
    path('', views.mostrar_especies, name='mostrar_especies'),
    path('agregar/', views.agregar_especies, name='agregar_especie')
]