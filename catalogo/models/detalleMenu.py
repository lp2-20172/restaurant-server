from django.db import models
from .menu import Menu


class DetalleMenu(models.Model):

    Menu = models.ForeignKey(Menu)
    cantidad = models.CharField(max_length=15)
    precioUni = models.FloatField(default=0.0)

    class Meta:
        verbose_name = "detalleMenu"
        verbose_name_plural = "detalleMenus"

    def __str__(self):
        return '%s (%s)' % (self.cantidad, self.precioUni,)
