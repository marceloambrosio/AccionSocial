from django.db import models
from datetime import date

# Create your models here.

class Barrio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    dni = models.IntegerField()
    barrio = models.ForeignKey(Barrio, on_delete=models.PROTECT)
    domicilio = models.CharField(max_length=200)
    telefono = models.IntegerField()

class Expediente(models.Model):
    fecha_carga = models.DateField(default=date.today)
    fecha_intervencion = models.DateField()
    numero_expediente = models.IntegerField()
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)