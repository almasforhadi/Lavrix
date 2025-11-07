from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CartItem
from .forms import CartAddForm
from shop.models import Product
from django.http import JsonResponse


# View: Show cart for current user(User Cart details)
@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, "cart_detail.html", {"cart_items": cart_items, "total": total})



#  AJAX: Add to cart
@login_required
def ajax_cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:   # only increase quantity if item already exists
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item.quantity = 1
        cart_item.save()

    # Return updated cart summary
    total = sum(item.total_price() for item in CartItem.objects.filter(user=request.user))
    count = CartItem.objects.filter(user=request.user).count()
    return JsonResponse({"success": True, "count": count, "total": total})



#  AJAX: Fetch current cart (for Drawer)
@login_required
def ajax_cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)

    data = {
        "items": [
            {
                "id": i.id,
                "name": i.product.name,
                "sale_price": float(i.product.sale_price),   # <-- send sale_price
                "quantity": i.quantity,
                "subtotal": i.total_price(),
                "image": i.product.images.first().image.url if i.product.images.exists() else "/static/images/no-image.jpg"
            }
            for i in cart_items
        ],
        "total": total
    }
    return JsonResponse(data)




#  AJAX: Update quantity (increase/decrease)
@login_required
def ajax_cart_update(request, item_id):
    action = request.GET.get("action")
    item = get_object_or_404(CartItem, id=item_id, user=request.user)

    if action == "increase":
        item.quantity += 1
    elif action == "decrease" and item.quantity > 1:
        item.quantity -= 1
    item.save()

    total = sum(i.total_price() for i in CartItem.objects.filter(user=request.user))
    return JsonResponse({"qty": item.quantity, "subtotal": item.total_price(), "total": total})


#  AJAX: Remove item
@login_required
def ajax_cart_remove(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()

    total = sum(i.total_price() for i in CartItem.objects.filter(user=request.user))
    count = CartItem.objects.filter(user=request.user).count()
    return JsonResponse({"success": True, "total": total, "count": count})

