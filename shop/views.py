from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Category, Product, ProductImage
from .forms import ProductForm, CategoryForm
from django.core.paginator import Paginator
from django.http import JsonResponse



def product_list(request):
    query = request.GET.get("q", "")
    category_slug = request.GET.get("category", None)
    sort_option = request.GET.get("sort", "")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")

    products = Product.objects.all().select_related("category")

    #  Search filter
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        )

    #  Category filter
    if category_slug:
        products = products.filter(category__slug=category_slug)

    #  Price Range filter
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    #  Sort filter
    if sort_option == "low-high":
        products = products.order_by("price")
    elif sort_option == "high-low":
        products = products.order_by("-price")
    elif sort_option == "featured":
        products = products.filter(featured=True)
    elif sort_option == "latest":
        products = products.order_by("-id")

    #  Pagination
    paginator = Paginator(products, 9)
    page_number = request.GET.get("page")
    products_page = paginator.get_page(page_number)

    categories = Category.objects.all()
    featured_products = Product.objects.filter(featured=True)[:6]

    # AJAX request → partial HTML return
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return render(request, "includes/_product_grid.html", {"products": products_page})

    # Full page render
    context = {
        "products": products_page,
        "categories": categories,
        "featured_products": featured_products,
        "query": query,
        "sort_option": sort_option,
        "min_price": min_price,
        "max_price": max_price,
    }
    return render(request, "product_list.html", context)






# Product Details Page
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    return render(request, "product_detail.html", {
        "product": product,
        "related_products": related_products,
    })




#  Category List Page
def category_list(request):
    categories = Category.objects.all()
    return render(request, "category_list.html", {"categories": categories})


