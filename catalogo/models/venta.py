from django.db import models
from .menu import Menu
from .producto import Producto
from .pedido import Pedido 


class Venta(models.Model):

    Menu = models.ForeignKey(Menu)
    cantidad = models.CharField(max_length=15)
    precioTotal = models.FloatField(default=0.0)
    pagado = models.CharField(max_length=15)
    Producto = models.ForeignKey(Producto)
    Pedido = models.ForeignKey(Pedido)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return '%s (%s) (%s)' % (self.cantidad, self.precioTotal, self.pagado,)
