from rest_framework import serializers
from ..models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    categoria = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='tipo'
    )
    imagen = serializers.ImageField()

    class Meta:
        model = Producto
        fields = '__all__' 