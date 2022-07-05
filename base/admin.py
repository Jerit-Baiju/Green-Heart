from django.contrib import admin
from .models import Product, ProductPack, ProductCategory

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductPack)
admin.site.register(ProductCategory)
