from django.http import HttpResponse
from django.shortcuts import render

from base.models import Company, ProductCategory, Product

from . import forms

# Create your views here.


def home(request):
    context = {}
    return render(request, 'admin/home.html', context)


def add_product(request):
    context = {
        'product_form': forms.ProductForm,
        'pack_form': forms.PackForm,
    }
    if request.method == 'POST':
        form1 = forms.ProductForm(request.POST, request.FILES)
        form2 = forms.PackForm(request.POST)
        # if form1.is_valid() and form2.is_valid():
        form1.save()
        form2.save()
            
    return render(request, 'admin/add_product.html', context)


def add_pack(request, pk):
    context = {
        'form': forms.PackForm,
        'product': Product.objects.get(pk=pk)
    }
    if request.method == 'POST':
        form = forms.PackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('SUCCESS')
        else:
            return HttpResponse('FAILED')
    return render(request, 'admin/add_pack.html', context)


def categories(request):
    context = {
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'admin/categories.html', context)
