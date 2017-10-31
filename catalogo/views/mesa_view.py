from ..models.mesa import Mesa
from rest_framework import serializers, viewsets
from rest_framework import permissions


class MesaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mesa
        fields = '__all__'


class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

