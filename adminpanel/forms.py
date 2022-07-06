from base import models 
from django.forms import ModelForm

class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'
        exclude = ['pack']
    

class PackForm(ModelForm):
    class Meta:
        model = models.ProductPack
        fields = '__all__'

class CategoryForm(ModelForm):
    class Meta:
        model = models.ProductCategory
        fields = '__all__'