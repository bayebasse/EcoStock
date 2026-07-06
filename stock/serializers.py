from django.utils import timezone
from rest_framework import serializers

from .models import Product, ProductStatus, Warehouse


class ProductSerializer(serializers.ModelSerializer):
    warehouse_name = serializers.CharField(
        source="warehouse.name",
        read_only=True
    )

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "quantity",
            "expiration_date",
            "status",
            "warehouse",
            "warehouse_name",
        )

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "La quantité ne peut pas être négative."
            )
        return value

    def validate_expiration_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError(
                "La date d'expiration est déjà dépassée."
            )
        return value

    def validate(self, data):
        warehouse = data["warehouse"]

        total = warehouse.products.exclude(
            pk=self.instance.pk if self.instance else None
        ).count()

        if total >= warehouse.capacity:
            raise serializers.ValidationError(
                "Cet entrepôt est déjà plein."
            )

        return data


class WarehouseSerializer(serializers.ModelSerializer):
    products = ProductSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Warehouse
        fields = (
            "id",
            "name",
            "location",
            "capacity",
            "products",
        )