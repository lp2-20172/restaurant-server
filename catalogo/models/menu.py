from django.db import models


class Menu(models.Model):

    nombre = models.CharField(max_length=30)
    precio = models.FloatField(default=0.0)
    imagen = models.ImageField( upload_to = 'photos/')

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return '%s (%s) (%s),' % (self.nombre, self.precio, self.imagen)
