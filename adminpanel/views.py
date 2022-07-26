from django.http import HttpResponse
from django.shortcuts import render

from base.models import Category, Company, Product, ProductPack



from . import forms

# Create your views here.


def home(request):
    context = {}
    return render(request, 'admin/home.html', context)


def add_product(request):
    pack_choices = ProductPack.pack_choices
    pack_types = []
    for choice in pack_choices:
        pack_types.append(choice[0])
    
    companies = Company.objects.all()
    categories = Category.objects.all()

    context = {
        'pack_types': pack_types,
        'companies': companies,
        'categories': categories
    }
    print(context)
    if request.method == 'POST':
        name = request.POST['name']
        company = request.POST['company']
        category = request.POST['category']
        quantity = request.POST['quantity']
        price = request.POST['price']
        image = request.FILES['image']
        pack_type = request.POST['pack_name']

        company_model, _ = Company.objects.get_or_create(company_name=company)
        category_model, _ = Category.objects.get_or_create(category=category)
        pack_model, _ = ProductPack.objects.get_or_create(quantity=quantity,price=price,pack_type=pack_type)
        product = Product.objects.create(name=name,image=image,category=category_model,company=company_model)
        product.pack.add(pack_model)

        return HttpResponse("Success")

            
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
        'categories': 'ProductCategory.objects.all()'
    }
    return render(request, 'admin/categories.html', context)
