from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, WarehouseViewSet

router = DefaultRouter()
router.register("warehouses", WarehouseViewSet)
router.register("products", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]