from django.urls import path
from usuario import  views

urlpatterns = [
    path('listar/usuario', views.ListarUsuario.as_view(), name='listar_usuarios'),
    path('agregar/usuario', views.RegistrarUsuario.as_view(), name='agregar_usuario'),
    path('deslogear/', views.desloguearce, name='deslogearce'),
    path('index/', views.index, name='index'),
    path('', views.login_view, name='login'),
    path('eliminar/usuario/<int:pk>', views.EliminarUsuario.as_view(), name='eliminar_usuario')
]