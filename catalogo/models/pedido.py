from django.db import models
from .menu import Menu
from .cliente import Cliente
from .mesa import Mesa


class Pedido(models.Model):

    menu = models.ForeignKey(Menu)
    confirmado = models.CharField(max_length=10)
    servido = models.CharField(max_length=10)
    cliente = models.ForeignKey(Cliente)
    mesa = models.ForeignKey(Mesa)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return '%s (%s) (%s)' % (self.fecha, self.confirmado,  self.servido,)
