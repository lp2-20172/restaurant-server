from ..models.detalleVenta import DetalleVenta
from rest_framework import serializers, viewsets
from rest_framework import permissions


class DetalleVentaSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetalleVenta
        fields = '__all__'


class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer
