from django.db import models
from .cliente import Cliente
from .mesa import Mesa


class Reserva(models.Model):

    cliente = models.ForeignKey(Cliente)
    mesa = models.ForeignKey(Mesa)
    finalizada = models.CharField(max_length=2)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return '%s' % (self.fecha)
