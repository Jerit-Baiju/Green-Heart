from django.db import models

# Create your models here.
class ProductPack(models.Model):
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Product(models.Model):
    name = models.CharField(max_length=30)
    packs = models.ForeignKey(ProductPack, on_delete=models.CASCADE)

