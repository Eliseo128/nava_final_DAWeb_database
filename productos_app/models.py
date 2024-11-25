from django.db import models

class Productos(models.Model):
    id_producto=models.CharField(primary_key=True,max_length=20)
    precio=models.DecimalField(decimal_places=2,max_digits=10000)
    marca=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20)
    categoria=models.CharField(max_length=20)
    diseño=models.CharField(max_length=60)
    calidad=models.CharField(max_length=60)
    def __str__(self):
        return self.nombre

# Create your models here.
