from django.urls import path
from flora import  views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required



urlpatterns = [
    # Urls de especie
    path('lista/especie/', login_required (views.ListarEspecie.as_view()), name='mostrar_especie'),
    path('agregar/especie/', login_required (views.RegistrarEspecie.as_view()), name='agregar_especie'),
    path('modificar/especie/<int:pk>', login_required (views.ModificarEspecie.as_view()), name='modificar_especie'),
    path('eliminar/especie/<int:pk>', login_required (views.EliminarEspecie.as_view()), name='eliminar_especie'),

    # Urls de zona
    path('lista/zona/', login_required (views.ListarZona.as_view()), name='mostrar_zona'),
    path('agregar/zona/',login_required (views.RegistrarZona.as_view()), name='agregar_zona'),
    path('modificar/zona/<int:pk>',login_required (views.ModificarZona.as_view()), name='modificar_zona'),
    path('eliminar/zona/<int:pk>', login_required (views.EliminarZona.as_view()), name='eliminar_zona'),
    #JSON BUSQUEDA
    path('buscar/zona/', views.buscar, name='buscar_especies'),
    path('buscar/especies/', views.buscar, name='buscar_especies'),
    #reportes
    path('reporte/zona/', views.generar_reporte_zona, name='reporte_zona'),
    path('reporte/especie/', views.generar_reporte_especie, name='reporte_especie')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)