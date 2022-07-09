from django.shortcuts import render

from base.models import Product, ProductPack


# Create your views here.


def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'base/index.html', context)


def product(request, category, pk):
    product_model = 'Product.objects.get(pk=pk)'
    # try:
    pack = ProductPack.objects.get(product=product_model)
    # except:
    #     pack = ''
    context = {
        'product': product_model,
        'category': category,
        'pack': pack,
    }
    return render(request, 'base/product.html', context)
