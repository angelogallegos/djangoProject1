from django.urls import path
from flora import  views

urlpatterns = [
    path('', views.mostrar_especie, name='mostrar_especie'),
    path('agregar/', views.agregar_especie, name='agregar_especie'),
    path('', views.mostrar_tipo_especie, name='mostrar_tipo_especie'),
    path('agregar/', views.agregar_tipo_especie, name='agregar_tipo_especie'),
    path('', views.mostrar_origen, name='mostrar_origen'),
    path('agregar/', views.agregar_origen, name='agregar_origen'),
    path('', views.mostrar_zona, name='mostrar_zona'),
    path('agregar/', views.agregar_zona, name='agregar_zona')

]