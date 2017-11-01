from ..models.detalleMenu import DetalleMenu
from rest_framework import serializers, viewsets
from rest_framework import permissions


class DetalleMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetalleMenu
        fields = '__all__'


class DetalleMenuViewSet(viewsets.ModelViewSet):
    queryset = DetalleMenu.objects.all()
    serializer_class = DetalleMenuSerializer
