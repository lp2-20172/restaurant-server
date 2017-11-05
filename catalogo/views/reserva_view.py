from ..models.reserva import Reserva
from rest_framework import serializers, viewsets
from rest_framework import permissions


class ReservaSerializer(serializers.ModelSerializer):
    cliente_nombres = serializers.SerializerMethodField()
    num_mesa = serializers.SerializerMethodField()

    class Meta:
        model = Reserva
        fields = '__all__'

    def get_cliente_nombres(self, obj):
        return "%s %s %s" % (obj.cliente.nombre,
                             obj.cliente.apePaterno,
                             obj.cliente.apeMaterno)

    def get_num_mesa(self, obj):
        return obj.mesa.numMesa


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
