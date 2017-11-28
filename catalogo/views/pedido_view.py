from ..models.pedido import Pedido
from rest_framework import serializers, viewsets
from rest_framework import permissions


class PedidoSerializer(serializers.ModelSerializer):
    cliente_nombres = serializers.SerializerMethodField()
    num_mesa = serializers.SerializerMethodField()
    menu_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Pedido
        fields = '__all__'
    def get_cliente_nombres(self, obj):
        return "%s %s %s" % (obj.cliente.nombre,
                             obj.cliente.apePaterno,
                             obj.cliente.apeMaterno)

    def get_num_mesa(self, obj):
        return obj.mesa.numMesa
    def get_menu_nombre(self, obj):
        return obj.menu.nombre

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
