from django.db import models

class Producto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    codigo_de_barras = models.CharField(max_length=20, unique=True, default='0')
    nombre = models.CharField(max_length=100)
    cantidad_existente = models.IntegerField()
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)


class RegistroSalida(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_salida = models.DateTimeField(auto_now_add=True)
