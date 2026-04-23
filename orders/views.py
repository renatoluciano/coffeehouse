from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from menu.models import Product
from .models import Order, OrderItem
from django.contrib import messages

# Função para checar se o usuário é funcionário
def is_staff(user):
    return user.is_staff or user.is_coffee_staff

@login_required
@user_passes_test(is_staff)
def barista_dashboard(request):
    # O comando correto é order_by (ordenar por data de criação decrescente)
    active_orders = Order.objects.exclude(status__in=['Delivered', 'Canceled']).order_by('-created_at')
    return render(request, 'orders/barista_dashboard.html', {'orders': active_orders})

@login_required
@user_passes_test(is_staff)
def update_status(request, order_id, new_status):
    order = get_object_or_404(Order, id=order_id)
    order.status = new_status
    order.save()
    messages.success(request, f"Order #{order.id} updated to {new_status}!")
    return redirect('barista_dashboard')

@login_required
def create_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    order = Order.objects.create(
        user=request.user,
        status='Pending',
        total_price=product.price
    )
    
    OrderItem.objects.create(
        order=order,
        product=product,
        quantity=1,
        price=product.price
    )
    
    messages.success(request, f'Order for {product.name} placed successfully!')
    return redirect('profile')
