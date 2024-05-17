from .views import ProductoViewSet


from rest_framework.routers import DefaultRouter
router = DefaultRouter()


router.register(r'productos', ProductoViewSet, basename='productos')