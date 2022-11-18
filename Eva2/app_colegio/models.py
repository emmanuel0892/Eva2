from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class alumnos (models.Model):
    rut = models.TextField(max_length=20, null=False)
    nombre = models.TextField(max_length=50, null=False)
    apellidos = models.TextField(max_length=50, null=False)
    sexo = models.TextField(max_length=50, null=False)
    curso = models.TextField(max_length=50, null=False)
    edad = models.IntegerField(validators=[MinValueValidator(5), MaxValueValidator(30)] ,null=False)
    ciudad = models.TextField(max_length=50, null=False)
    comuna = models.TextField(max_length=50, null=False)