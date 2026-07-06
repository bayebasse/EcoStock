from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class ProductStatus(models.TextChoices):
    AVAILABLE = "disponible", "Disponible"
    RESERVED = "reserve", "Réservé"
    EXPIRED = "perime", "Périmé"




class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    expiration_date = models.DateField()
    status = models.CharField(max_length=20, choices=ProductStatus.choices, default=ProductStatus.AVAILABLE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name="products")

    def clean(self):
        if self.expiration_date < timezone.now().date():
            self.status = ProductStatus.EXPIRED

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)        

    def __str__(self):
        return self.name    

