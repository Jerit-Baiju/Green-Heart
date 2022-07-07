from django.db import models

# Create your models here.


class ProductPack(models.Model):
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} LTR"


class ProductCategory(models.Model):
    category = models.CharField(max_length=50, unique=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class ProductCompany(models.Model):
    company = models.CharField(max_length=50, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True,
                              upload_to='product_images')

    def __str__(self):
        return self.name
