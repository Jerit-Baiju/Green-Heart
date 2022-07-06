from django.db import models

# Create your models here.


class ProductPack(models.Model):
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} LTR"


class ProductCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to='Products')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    pack = models.ManyToManyField(ProductPack)
    company = models.CharField(null=True, blank=True, max_length=50, unique=True)

    def __str__(self):
        return self.name
