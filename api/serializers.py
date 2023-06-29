from rest_framework import serializers
from crud.models import Producto, Marca
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('idProducto', 'descripcion', 'precio', 'stock', 'marca')


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('idMarca', 'marca')

