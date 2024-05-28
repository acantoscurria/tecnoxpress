from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from .serializers import (
    ProductoSerializer, 
    CategoriaSerializer,
    ProductoCategoriaSerializer
    )
from apps.productos.models import Categoria, Producto


class ProductoViewSet(ModelViewSet):
 
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = ProductoCategoriaSerializer
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = ProductoCategoriaSerializer
        return super().retrieve(request, *args, **kwargs)

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    # permission_classes = [DjangoModelPermissions]
    serializer_class = CategoriaSerializer