from django.http import HttpResponse
from django.shortcuts import render

from base.models import ProductCategory

from . import forms

# Create your views here.

def home(request):
    context = {}
    return render(request, 'admin/home.html', context)

def add_product(request):
    context = {
        'form' : forms.ProductForm
    }
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('SUCCESS')
        else:
            return HttpResponse('FAILED')
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
    if request.method == 'POST':
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('SUCCESS')
        else:
            return HttpResponse('FAILED')
    return render(request,'admin/add_category.html', context)

def categories(request):
    context = {
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'admin/categories.html', context)