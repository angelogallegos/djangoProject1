from django.urls import path
from usuario import  views

urlpatterns = [
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('agregar/', views.agregar_usuario, name='agregar_usuario')
]