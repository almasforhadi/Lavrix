from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from orders.models import Order
from shop.models import Product
from blog.models import BlogPost
from django.contrib import messages


def home(request):
    products = Product.objects.all()
    blog_posts = BlogPost.objects.filter(is_published=True)[:3]

    # Add the first image for each product
    for product in products:
        if product.images.exists():
            product.image_url = product.images.first().image.url
        else:
            product.image_url = None  # fallback if no image

    return render(request, 'home.html', {'products': products, 'blog_posts': blog_posts})



def contact(request):
    return render(request, 'contact.html')


def service(request):
    return render(request, 'service.html')



@login_required
def dashboard(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    user = request.user

    if request.method == "POST":
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")

        password = request.POST.get("password")

        if password:
            user.set_password(password)
            user.save()
            update_session_auth_hash(request, user)
        else:
            user.save()

        messages.success(request, "Your account has been updated successfully!")
        return redirect("dashboard")

    context = {
        "total_orders": orders.count(),
        "pending_orders": orders.filter(status="pending").count(),
        "completed_orders": orders.filter(status="delivered").count(),
        "wishlist_count": 5,
        "recent_orders": orders[:5],
        "wishlist": [],
    }
    return render(request, "dashboard.html", context)



