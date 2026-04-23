from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from menu.models import Product
from menu.cart import Cart
from .models import Order, OrderItem

def is_staff(user):
    return user.is_staff or user.is_coffee_staff

@login_required
def create_order(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.error(request, "Your cart is empty!")
        return redirect('index')

    # Create the main Order
    order = Order.objects.create(
        user=request.user,
        status='Pending',
        total_price=cart.get_total_price()
    )

    # Transfer items from Cart to OrderItem
    for item in cart:
        OrderItem.objects.create(
            order=order,
            product=item['product'],
            price=item['price'],
            quantity=item['quantity']
        )

    # Clear the cart after placing order
    cart.clear()

    messages.success(request, f'Order #{order.id} placed successfully! Barista is on it. ☕')
    return redirect('profile')

@login_required
@user_passes_test(is_staff)
def barista_dashboard(request):
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
