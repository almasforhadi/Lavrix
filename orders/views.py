from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from .forms import OrderStatusForm


#  Show all orders for admin or current user
@login_required
def order_list(request):
    if request.user.is_staff:
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(user=request.user)
    return render(request, "order_list.html", {"orders": orders})


#  Show a specific order detail (with items)
@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.user != order.user and not request.user.is_staff:
        messages.error(request, "You are not authorized to view this order.")
        return redirect("orders:order_list")

    return render(request, "order_detail.html", {"order": order})


# Update order status (admin only)
@login_required
def update_order_status(request, order_id):
    if not request.user.is_staff:
        messages.error(request, "Only admins can update order status.")
        return redirect("orders:order_list")

    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, f"Order #{order.id} status updated successfully.")
            return redirect("orders:order_detail", order_id=order.id)
    else:
        form = OrderStatusForm(instance=order)

    return render(request, "order_status_form.html", {"form": form, "order": order})


# /*-------------------order_history-----------------*/
@login_required
def order_history(request):
    """Logged-in user's order history"""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "order_history.html", {"orders": orders})

