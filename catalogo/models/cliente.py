from django.db import models


class Cliente(models.Model):

    nombre = models.CharField(max_length=60)
    apePaterno = models.CharField(max_length=60)
    apeMaterno = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    telefono = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return '%s (%s) (%s)' % (self.nombre, self.apePaterno, self.apeMaterno)
