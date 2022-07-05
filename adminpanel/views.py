from django.shortcuts import render
from . import forms

# Create your views here.

def home(request):
    context = {}
    return render(request, 'admin/home.html', context)

def add_product(request):
    context = {
        'form' : forms.ProductForm
    }
    return render(request, 'admin/add_product.html', context)

def add_pack(request):
    context = {
        'form' : forms.PackForm
    }
    return render(request,'admin/add_pack.html', context)

def add_category(request):
    context = {
        'form' : forms.CategoryForm
    }
    return render(request,'admin/add_category.html', context)