from django.db import models

# Create your models here.
class Usuario(models.Model):
    Nombre = models.CharField(max_length=50, blank=False)
    Correo = models.CharField(max_length=100, blank=False)
    Direccion = models.CharField(max_length=50, blank=False)
    Usuario = models.CharField(max_length=20, blank=False)
    Contraseña = models.CharField(max_length=30, blank=False)

    def __int__(self):
        return self.id