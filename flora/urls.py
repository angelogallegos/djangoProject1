from django.urls import path
from flora import  views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('lista/especie/', login_required (views.ListarEspecie.as_view()), name='mostrar_especie'),
    path('agregar/especie/', login_required (views.RegistrarEspecie.as_view()), name='agregar_especie'),
    path('modificar/especie/<int:pk>', login_required (views.ModificarEspecie.as_view()), name='modificar_especie'),
    path('eliminar/especie/<int:pk>', login_required (views.EliminarEspecie.as_view()), name='eliminar_especie'),

    # urls de zona
    path('lista/zona/', views.ListarZona.as_view(), name='mostrar_zona'),
    path('agregar/zona/', views.RegistrarZona.as_view(), name='agregar_zona'),
    path('modificar/zona/<int:pk>', views.ModificarZona.as_view(), name='modificar_zona'),
    path('eliminar/zona/<int:pk>', views.EliminarZona.as_view(), name='eliminar_zona')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)