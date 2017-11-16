from django.db import models
from .cliente import Cliente
from .pedido import Pedido 


class Venta(models.Model):

    precioTotal = models.FloatField(default=0.0)
    Pedido = models.ForeignKey(Pedido)
    Cliente = models.ForeignKey(Cliente)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return '%s (%s)' % (self.precioTotal, self.fecha,)
