from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .cart import Cart # Importa a nossa nova classe

def index(request):
    products = Product.objects.all()
    return render(request, 'menu/index.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'menu/product_detail.html', {'product': product})

# --- NOVAS VIEWS DO CARRINHO ---

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'menu/cart_detail.html', {'cart': cart})
