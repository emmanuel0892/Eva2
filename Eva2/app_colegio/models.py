from pyexpat import model
from django.db import models

class alumnos (models.Model):
    nombre = models.TextField(max_length=50, null=False)
    apePaterno = models.TextField(max_length=50, null=False)
    apeMaterno = models.TextField(max_length=50, null=False)
    sexo = models.TextField(max_length=50, null=False)
    curso = models.TextField(max_length=50, null=False)
    edad = models.IntegerField(null=False)
    ciudad = models.TextField(max_length=50, null=False)
    comnuna = models.TextField(max_length=50, null=False)