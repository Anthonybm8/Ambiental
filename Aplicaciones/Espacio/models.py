from django.db import models

# Create your models here.
class Espacio(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.tipo}"