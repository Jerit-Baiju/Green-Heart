from django.http import HttpResponse
from django.shortcuts import render

from base.models import Company, ProductCategory, Product, ProductPack

from . import forms

# Create your views here.


def home(request):
    context = {}
    return render(request, 'admin/home.html', context)


def add_product(request):
    context = {
        'categories': ProductCategory.objects.all(),
        'companies': Company.objects.all()
    }
    if request.method == 'POST':
        name = request.POST['name']
        company = request.POST['company']
        image = request.FILE['image']
        category = request.POST['category']
        quantity = request.POST['quantity']
        price = request.POST['price']

        pack = ProductPack.objects.create(quantity=quantity, price=price)
        category = ProductCategory.objects.create(name=category)
        company = Company.objects.create(name=company)
        product = Product.objects.create(
            name=name, company=company, image=image, pack=pack, category=category)

        product.save()
        return HttpResponse('SUCCESS')
        
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
