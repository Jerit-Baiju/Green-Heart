from django.db import models

# Create your models here.
class ProductPack(models.Model):
    name = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} LTR"
    
class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True, default='product.jpg')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

