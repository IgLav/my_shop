from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)

