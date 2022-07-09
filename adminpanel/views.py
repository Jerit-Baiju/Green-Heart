from django.http import HttpResponse
from django.shortcuts import render

from base.models import Company, ProductPack



from . import forms

# Create your views here.


def home(request):
    context = {}
    return render(request, 'admin/home.html', context)


def add_product(request):
    context = {
        'pack_types': ProductPack.pack_choices
    }
    print(context)
    if request.method == 'POST':
        name = request.POST['name']
        company = request.POST['company']
        category = request.POST['category']
        quantity = request.POST['quantity']
        price = request.POST['price']
        image = request.FILES['image']
        pack_type = request.POST['']

        company_model = Company.objects.get_or_create(company_name=company)

            
    return render(request, 'admin/add_product.html', context)


def add_pack(request, pk):
    context = {
        'form': forms.PackForm,
        'product': 'Product.objects.get(pk=pk)'
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
