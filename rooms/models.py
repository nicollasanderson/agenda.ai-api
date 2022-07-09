from django.db import models

# Create your models here.

class TypeChoices(models.TextChoices):
    LABORATORIO = ('Laboratório')
    SALAAULA = ('Sala de Aula')

class Room(models.Model):
    room_type = models.CharField(max_length=50,choices=TypeChoices.choices,default=TypeChoices.SALAAULA)
    block = models.IntegerField()
    name = models.CharField(max_length=100)