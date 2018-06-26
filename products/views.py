from django.shortcuts import render
from .models import Product

def get_products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html',{'products': products})
    