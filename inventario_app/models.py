from django.db import models

# Create your models here.

class Inventario(models.Model):
    id_inventario=models.CharField(primary_key=True,max_length=100)
    fecha_entrada=models.DateTimeField()
    estado_producto=models.CharField(max_length=30)
    codigo_barras=models.IntegerField()
    cantidad_stock=models.IntegerField()
    descripcion=models.TextField()
    precio_unitario=models.DecimalField(max_digits=100,decimal_places=2)
    def _str_(self) -> str:
        return f"ID inventario: {self.id_inventario}"
    
