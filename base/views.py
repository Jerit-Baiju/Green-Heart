from django.http import HttpResponse
from django.shortcuts import render

from base.models import Product, ProductPack

# Create your views here.

def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'base/index.html', context)

def categories(request,category):
    context = {
        'products': Product.objects.get(category=category)
    }
    return render(request,context)

# def product(request, collection, pk):
#     return render(request)