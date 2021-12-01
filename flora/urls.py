from django.urls import path
from flora import  views

urlpatterns = [
    path('lista/especie/', views.ListarEspecie.as_view(), name='mostrar_especie'),
    path('agregar/especie/', views.RegistrarEspecie.as_view(), name='agregar_especie'),
    path('modificar/especie/<int:pk>', views.ModificarEspecie.as_view(), name='modificar_especie'),
    path('eliminar/especie/<int:pk>', views.EliminarEspecie.as_view(), name='eliminar_especie'),

    # urls de zona
    path('lista/zona/', views.ListarZona.as_view(), name='mostrar_zona'),
    path('agregar/zona/', views.RegistrarZona.as_view(), name='agregar_zona'),
    path('modificar/zona/<int:pk>', views.ModificarZona.as_view(), name='modificar_zona'),
    path('eliminar/zona/<int:pk>', views.EliminarZona.as_view(), name='eliminar_zona')

]