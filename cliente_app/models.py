from django.db import models

# Create your models here.

class Cliente(models.Model):
    id_cliente=models.CharField(primary_key=True,max_length=30)
    nombre=models.CharField(max_length=20)
    pago_total=models.DecimalField(max_digits=100,decimal_places=2)
    telefono=models.IntegerField()
    hora_compra=models.TimeField()
    cantidad_productos=models.IntegerField()
    dia_compra=models.DateTimeField()
    def __str__(self) -> str:
        return self.nombre
