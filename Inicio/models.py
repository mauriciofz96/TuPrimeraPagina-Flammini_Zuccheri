from django.db import models

# Create your models here.

class Musico(models.Model):
    nombre = models.CharField(max_length = 30)
    instrumento = models.CharField(max_length = 30)
    banda = models.CharField(max_length = 30)

class Album(models.Model):
    nombre_disco = models.CharField(max_length = 30)
    banda = models.CharField(max_length = 30)
    lanzamiento = models.IntegerField()
    genero = models.CharField(max_length = 30)

class Banda(models.Model):
    nombre = models.CharField(max_length=100)
    integrantes = models.IntegerField()
