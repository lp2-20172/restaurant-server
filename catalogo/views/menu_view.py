from ..models.menu import Menu
from rest_framework import serializers, viewsets
from rest_framework import permissions


class MenuSerializer(serializers.ModelSerializer):
    # campo_nuevo = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')

    # def get_campo_nuevo(self, obj):
    #     # return "%s %s " % (obj.codigo, obj.nombre)
    #     return dict(
    #         nombre="dewdew"
    #         )


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
