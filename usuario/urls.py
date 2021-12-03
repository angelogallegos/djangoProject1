from django.urls import path
from usuario import  views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listar/usuario', views.ListarUsuario.as_view(), name='listar_usuarios'),
    path('agregar/usuario', views.RegistrarUsuario.as_view(), name='agregar_usuario'),
    path('deslogear/', views.desloguearce, name='deslogearce'),
    path('index/', views.index, name='index'),
    path('', views.login_view, name='login'),
    path('eliminar/usuario/<int:pk>', views.EliminarUsuario.as_view(), name='eliminar_usuario'),
    path('modificar/usuario/<int:pk>', views.ModificarUsuario.as_view(), name='modificar_usuario')
]