from django.db import models
from .menu import Menu
from .producto import Producto


class Venta(models.Model):

    Menu = models.ForeignKey(Menu)
    cantidad = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    precioTotal = models.FloatField(default=0.0)
    servida = models.CharField(max_length=15)
    pagado = models.CharField(max_length=15)
    Producto = models.ForeignKey(Producto)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return '%s (%s) (%s) (%s) (%s)' % (self.cantidad, self.nombre, self.precioTotal, self.servida, self.pagado,)
