from django.shortcuts import render

from base.models import Product, ProductPack

# Create your views here.

def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'base/index.html', context)

def 