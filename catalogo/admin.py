from django.contrib import admin
from .models.producto import Producto
from .models.reserva import Reserva
from .models.venta import Venta
from .models.cliente import Cliente
from .models.mesa import Mesa
from .models.pedido import Pedido
from .models.menu import Menu
from .models.detalleMenu import DetalleMenu

# Register your models here.


class ReservaAdmin(admin.ModelAdmin):
    """docstring for ProductoAdmin"""
    list_per_page = 2
    list_display = ("fecha", "finalizada",
                    "cliente_nombre", "mesa_numMesa",)
    search_fields = ("fecha", "finalizada",)

    def cliente_nombre(self, obj):
        return obj.cliente.nombre

    def mesa_numMesa(self, obj):
        return obj.mesa.numMesa


admin.site.register(Reserva, ReservaAdmin)


class ClienteAdmin(admin.ModelAdmin):
    """docstring for ProductoAdmin"""
    list_display = ("nombre", "apePaterno", "apeMaterno",)

    search_fields = ("nombre", "apePaterno", "apeMaterno",)

admin.site.register(Cliente, ClienteAdmin)


class MesaAdmin(admin.ModelAdmin):
    """docstring for ProductoAdmin"""
    list_display = ("piso", "maxPersonas", "numMesa", "libre",)

    search_fields = ("piso", "maxPersonas", "numMesa", "libre",)

admin.site.register(Mesa, MesaAdmin)


class detalleMenuAdmin(admin.ModelAdmin):

    list_display = ("cantidad", "precioUni",
                    "menu_nombre",)

    search_fields = ("cantidad", "precioUni",)

    def menu_nombre(self, obj):
        return obj.menu.nombre


admin.site.register(DetalleMenu, detalleMenuAdmin)


class MenuAdmin(admin.ModelAdmin):

    list_display = ("nombre", "precio")

    search_fields = ("nombre", "precio",)


admin.site.register(Menu, MenuAdmin)


class VentaAdmin(admin.ModelAdmin):

    list_display = ("cantidad", "nombre", "precioTotal", "servida",
                    "pagado", "Menu_nombre", "Producto_nombre",)

    search_fields = ("cantidad", "nombre", "precioTotal",
                     "servida", "pagado",)

    def Menu_nombre(self, obj):
        return obj.Menu.nombre

    def Producto_nombre(self, obj):
        return obj.Producto.nombre

admin.site.register(Venta, VentaAdmin)


class PedidoAdmin(admin.ModelAdmin):

    list_display = ("fecha", "confirmado", "servido",
                    "cliente_nombre", "mesa_numMesa", "menu_nombre")
    search_fields = ("fecha", "confirmado", "servido",)

    def cliente_nombre(self, obj):
        return obj.cliente.nombre

    def mesa_numMesa(self, obj):
        return obj.mesa.numMesa

    def menu_nombre(self, obj):
        return obj.menu.nombre

admin.site.register(Pedido, PedidoAdmin)


class ProductoAdmin(admin.ModelAdmin):

    list_display = ("nombre", "tipoProducto",
                    "cantidad", "precio", "uniMedida",)

    search_fields = ("nombre", "tipoProducto",
                     "cantidad", "precio", "uniMedida",)


admin.site.register(Producto, ProductoAdmin)
