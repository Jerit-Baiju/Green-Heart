from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Company(models.Model):
    company_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.company_name


class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category


class ProductPack(models.Model):
    quantity = models.DecimalField(max_digits=10, default=1, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pack_choices = (
        ("KG", "KG"),
        ("LTR", "LTR"),
        ("ML", "ML")
    )
    pack_type = models.CharField(
        max_length=10, choices=pack_choices, default='LTR')

    def __str__(self):
        return f"{self.quantity} {self.pack_type}"


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='Products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    pack = models.ManyToManyField(ProductPack)

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class User(AbstractUser):
    name = models.CharField(max_length=200)
    cart = models.ManyToManyField(CartProduct)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    # username = models.CharField(unique=True, max_length=200, null=True)
    # email = models.EmailField(max_length=200)
    # log = models.TextField(null=True, blank=True)
    # score = models.IntegerField(null=True, blank=True)
    # USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
