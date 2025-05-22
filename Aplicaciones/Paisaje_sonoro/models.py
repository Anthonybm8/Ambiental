from django.db import models
from Aplicaciones.Empleado.models import Empleado
from Aplicaciones.Espacio.models import Espacio

# Create your models here.
class PaisajeSonoro(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    duracion = models.DurationField()
    descripcion = models.TextField(blank=True)

    artista = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)