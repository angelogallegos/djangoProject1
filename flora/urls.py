from django.urls import path
from flora import  views

urlpatterns = [
    path('', views.mostrar_especie, name='mostrar_especie'),
    path('agregar/', views.agregar_especie, name='agregar_especie'),

    # urls de zona
    path('lista/zona', views.ListarZona.as_view(), name='mostrar_zona'),
    path('agregar/zona/', views.RegistrarZona.as_view(), name='agregar_zona'),
    path('modificar/zona/<int:pk>', views.ModificarZona.as_view(), name='modificar_zona'),
    path('eliminar/zona/<int:pk>', views.EliminarZona.as_view(), name='eliminar_zona')

]