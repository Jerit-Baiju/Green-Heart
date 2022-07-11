from django.shortcuts import render

from base.models import Product

# Create your views here.


def index(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'base/index.html', context)


def product(request, category, pk):
    product_model = Product.objects.get(pk=pk)
    packs = product_model.pack.all()
    context = {
        'product': product_model,
        'category': category,
        'packs': packs,
        'main': packs[0].price
    }
    if request.method == "POST":
        None
    return render(request, 'base/product.html', context)
