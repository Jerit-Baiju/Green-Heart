from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'admin/home.html', context)

def add_product(request):
    context = {}
    return render(request, 'admin/add_product.html', context)