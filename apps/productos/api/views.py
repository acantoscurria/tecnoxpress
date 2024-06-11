from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from .serializers import (
    ProductoSerializer, 
    CategoriaSerializer,
    ProductoCategoriaSerializer
    )
from apps.productos.models import Categoria, Producto
from drf_spectacular.utils import extend_schema, OpenApiParameter


class ProductoViewSet(ModelViewSet):
 
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    # permission_classes = [DjangoModelPermissions]

    @ extend_schema(
        parameters=[
            OpenApiParameter(
                name='categoria_id', description='Buscar por categoria', required=False, type=str),
        ],
    )
    def list(self, request, *args, **kwargs):
        self.serializer_class = ProductoCategoriaSerializer

        nombre = request.GET.get('categoria_id')
        if nombre:
            self.queryset = self.queryset.filter(categoria_id=nombre)

        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = ProductoCategoriaSerializer
        return super().retrieve(request, *args, **kwargs)


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    # permission_classes = [DjangoModelPermissions]
    serializer_class = CategoriaSerializer