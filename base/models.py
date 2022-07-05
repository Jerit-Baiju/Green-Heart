from django.db import models

# Create your models here.
class ProductPacks(models.Model):
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} LTR"
    
class ProductCategories(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True, default='product.jpg')
    pack = models.ForeignKey(ProductPacks, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

