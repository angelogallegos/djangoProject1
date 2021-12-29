import uuid

from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from random import random

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
    Imagen1 = models.ImageField(upload_to="Imagenes", blank=True, null=True, default='')
    Imagen2 = models.ImageField(upload_to="Imagenes", blank=True, null=True, default='')
    Imagen3 = models.ImageField(upload_to="Imagenes", blank=True, null=True, default='')
    Zona = models.ManyToManyField(to='flora.Zona',through='flora.Ubicacion')
    QR = models.UUIDField(default=uuid.uuid4, unique=True, max_length=50)
    qr_code = models.ImageField(upload_to="qr_codes", blank=True, null=True, default='')
    Localizacion = models.CharField(max_length=900, blank=False, null=False, default='')

    def __int__(self):
        return self.id

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.QR)
        canvas = Image.new('RGB', (380, 380), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.QR}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


class Tipo(models.Model):
    Nombre = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.Nombre

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

