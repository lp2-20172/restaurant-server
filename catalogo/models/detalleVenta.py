from django.db import models
from .venta import Venta
from .menu import Menu
from .producto import Producto


class DetalleVenta(models.Model):

    Menu = models.ForeignKey(Menu)
    Venta = models.ForeignKey(Venta)
    Producto = models.ForeignKey(Producto)
    cantidad = models.CharField(max_length=15)
    precioUni = models.FloatField(default=0.0)
    precioTotal = models.FloatField(default=0.0)

    class Meta:
        verbose_name = "detalleVenta"
        verbose_name_plural = "detalleVentas"

    def __str__(self):
        return '%s (%s) (%s)' % (self.cantidad, self.precioUni, self.precioTotal)
