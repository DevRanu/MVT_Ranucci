from django.db import models

# Create your models here.

class Hermano(models.Model):
    nombre=models.CharField(max_length=40)
    edad=models.IntegerField()
    nacido=models.DateField(max_length=20)

class Primo(models.Model):
    nombre=models.CharField(max_length=40)
    edad=models.IntegerField()
    nacido=models.DateField(max_length=20)

class Sobrino(models.Model):
    nombre=models.CharField(max_length=40)
    edad=models.IntegerField()
    nacido=models.DateField(max_length=20)