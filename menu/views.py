from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all() # Fetching all coffee items
    return render(request, 'menu/index.html', {'products': products})
