from django.contrib import admin
from .models import Especie, Tipo, Zona, Ubicacion, Imagen, Tolerancia_Frio, Estado, Humedad_Suelo, Origen, Luminosidad
# Register your models here.
admin.site.register(Especie)
admin.site.register(Tipo)
admin.site.register(Zona)
admin.site.register(Ubicacion)
admin.site.register(Imagen)
admin.site.register(Tolerancia_Frio)
admin.site.register(Estado)
admin.site.register(Humedad_Suelo)
admin.site.register(Origen)
admin.site.register(Luminosidad)
