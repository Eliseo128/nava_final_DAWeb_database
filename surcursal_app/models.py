from django.db import models

# Create your models here.

class Sucursales(models.Model):
    id_surcursal=models.CharField(primary_key=True,max_length=20)
    ubicacion=models.CharField(max_length=30)
    tamaño=models.DecimalField(max_digits=10000,decimal_places=2)
    capacidad=models.IntegerField()
    gerente=models.CharField(max_length=30)
    horario=models.TimeField()
    telefono=models.IntegerField()
    def _str_(self) -> str:
        return f"ID surcursal: {self.id_surcursal}"