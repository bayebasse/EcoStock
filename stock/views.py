from django.db.models import Count
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Product, Warehouse
from .serializers import ProductSerializer, WarehouseSerializer


class WarehouseViewSet(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=["get"])
    def audit(self, request, pk=None):
        warehouse = self.get_object()
        total = warehouse.products.aggregate(total=Count("id"))

        return Response(
            {
                "warehouse": warehouse.name,
                "total_products": total["total"]
            }
        )


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related("warehouse")
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=["post"])
    def move(self, request, pk=None):
        product = self.get_object()
        warehouse_id = request.data.get("warehouse")
        if product.expiration_date < timezone.now().date():
            return Response(
                {
                    "message": "Impossible de déplacer un produit périmé."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            warehouse = Warehouse.objects.get(pk=warehouse_id)
        except Warehouse.DoesNotExist:
            return Response(
                {
                    "message": "Entrepôt introuvable."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        product.warehouse = warehouse
        product.save()
        return Response(
            {
                "message": "Produit transféré avec succès."
            },
            status=status.HTTP_200_OK
        )