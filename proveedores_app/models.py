from django.db import models

# Create your models here.

class Proveedores(models.Model):
    id_proveedor=models.CharField(primary_key=True,max_length=30)
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    tipo_producto=models.CharField(max_length=20)
    horario=models.TimeField()
    telefono=models.IntegerField()
    direccion=models.CharField(max_length=40)
    def __str__(self) -> str:
        return self.nombre