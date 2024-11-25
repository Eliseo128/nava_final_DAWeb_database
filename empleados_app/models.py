from django.db import models

# Create your models here.

class Empleados(models.Model):
    id_empleados=models.IntegerField()
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    curp=models.CharField(max_length=18)
    telefono=models.IntegerField()
    horario=models.TimeField()
    paga=models.DecimalField(max_digits=1000,decimal_places=2)
    def _str_(self) -> str:
        return self.nombre