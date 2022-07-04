from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'products' : [
            {
                'name': 'product 1',
                'img': ''
            }
        ]
    }
    return render(request, 'base/index.html', context)