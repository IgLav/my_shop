from django.shortcuts import render
from .models import *


# Create your views here.

def product_list(request):
    products = Product.objects.filter(available=True)
    context = {
        'products': products
    }
    return render(request, 'product_list.html', context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)
