from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=50, unique=True)

class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category
    

class Product_Pack(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    pack_type = models.TextChoices('KG','LTR')

    def __str__(self):
        return f"{self.quantity} {self.pack_type}"
    

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='Products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # pack = models.ManyToManyField(Product_Pack)

    def __str__(self):
        return self.name