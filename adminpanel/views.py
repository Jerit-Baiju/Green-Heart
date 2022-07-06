from django.http import HttpResponse
from django.shortcuts import render

from base.models import ProductCategory, Product

from . import forms

# Create your views here.

def home(request):
    context = {}
    return render(request, 'admin/home.html', context)

def add_product(request):
    context = {
        
    }
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('SUCCESS')
        else:
            return HttpResponse('FAILED')
    return render(request, 'admin/add_product.html', context)

def add_pack(request, pk):
    context = {
        'form' : forms.PackForm,
        'product': Product.objects.get(pk=pk)
    }
    if request.method == 'POST':
        form = forms.PackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('SUCCESS')
        else:
            return HttpResponse('FAILED')
    return render(request,'admin/add_pack.html', context)


def categories(request):
    context = {
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'admin/categories.html', context)