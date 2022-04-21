from django.db import models

# Create your models here.

from django.db import models

class Motos(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()

class cliente(models.Model):
    nome = models.CharField(max_length=150)
    cidade = models.CharField(max_length=100)
