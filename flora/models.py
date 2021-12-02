from django.db import models

# Create your models here.
class Especie(models.Model):
    Nombre = models.CharField(max_length=20, blank=False, null=False, default='')
    Nombre_Cientifico = models.CharField(max_length=50, blank=False, null=False, default='')
    Autor = models.CharField(max_length=20, blank=True, null=True, default='')
    Origen = models.ForeignKey(to='flora.Origen', on_delete=models.CASCADE, default='')
    Pais = models.CharField(max_length=35, blank=True, null=True, default='')
    Altura = models.CharField(max_length=10, blank=False, null=False, default='')
    Tipo = models.ForeignKey(to='flora.Tipo', on_delete=models.CASCADE, default='')
    Estado = models.ForeignKey(to='flora.Estado', on_delete=models.CASCADE, default='')
    Luminosidad = models.ForeignKey(to='flora.Luminosidad', on_delete=models.CASCADE, default='')
    Tolerancia_Frio = models.ForeignKey(to='flora.Tolerancia_Frio', on_delete=models.CASCADE, default='')
    Humedad_Suelo = models.ForeignKey(to='flora.Humedad_Suelo', on_delete=models.CASCADE, default='')
    Hojas = models.CharField(max_length=50, blank=False, null=False, default='')
    Flores = models.CharField(max_length=50, blank=False, null=False, default='')
    Semillas = models.CharField(max_length=50, blank=False, null=False, default='')
    Imagen_Perfil = models.ImageField(upload_to="Imagen_Perfil", null=True, default='')
    Imagen = models.ForeignKey(to='flora.Imagen', on_delete=models.CASCADE, default='')
    Zona = models.ManyToManyField(to='flora.Zona',through='flora.Ubicacion')
    QR = models.CharField(max_length=100, blank=True, null=True, default='')
    Imagen_QR = models.CharField(max_length=100, blank=True, null=True, default='')
    Longitud = models.CharField(max_length=100, blank=True, null=True, default='')
    Latitud = models.CharField(max_length=100, blank=True, null=True, default='')

    def __int__(self):
        return self.id


class Tipo(models.Model):
    Nombre = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.Nombre

class Imagen(models.Model):
    Nombre = models.CharField(max_length=20, blank=True, null=True)

    def __int__(self):
        return self.id

class Tolerancia_Frio(models.Model):
    Nombre = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.Nombre

class Humedad_Suelo(models.Model):
    Nombre = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.Nombre

class Origen(models.Model):
    Nombre = models.CharField(max_length=20, blank=False)
    def __str__(self):
        return self.Nombre

class Zona(models.Model):
    Nombre = models.CharField(max_length=60,blank=False, unique=True)
    Descripcion = models.CharField(max_length=200, blank=False)
    Especie = models.ManyToManyField(to='flora.Especie', through='flora.Ubicacion')
    def __str__(self):
        return self.Nombre


class Ubicacion(models.Model):
    Zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    Especie = models.ForeignKey(Especie, on_delete=models.CASCADE, default=None)

    def __int__(self):
        return self.id

class Luminosidad(models.Model):
    Nombre = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.Nombre

class Estado(models.Model):
    Nombre = models.CharField(max_length=40, blank=False)

    def __str__(self):
        return self.Nombre