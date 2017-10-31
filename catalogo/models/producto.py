from django.db import models


class Producto(models.Model):

    nombre = models.CharField(max_length=60)
    tipoProducto = models.CharField(max_length=15)
    uniMedida = models.CharField(max_length=15)
    cantidad = models.CharField(max_length=60)
    precio = models.FloatField(default=0.0)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return '%s (%s) (%s) (%s) (%s)' % (self.nombre, self.tipoProducto, self.cantidad, self.cantidad, self.precio,)