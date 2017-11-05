from django.db import models


class Mesa(models.Model):

    piso = models.CharField(max_length=100)
    maxPersonas = models.CharField(max_length=60)
    numMesa = models.CharField(max_length=60)
    libre = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Mesa"
        verbose_name_plural = "Mesas"

    def __str__(self):
        return '%s (%s) (%s) (%s)' % (self.piso, self.maxPersonas, self.numMesa, self.libre,)
