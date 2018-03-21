from django.db import models


# Create your models here.
class Tarea(models.Model):
    nombre = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    fecha = models.DateField()
    completada = models.BooleanField()
