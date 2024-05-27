from rest_framework import *
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from .serializers import ProductoSerializer
from apps.productos.models import Producto


class ProductoViewSet(viewsets.ModelViewSet):
 
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [DjangoModelPermissions]