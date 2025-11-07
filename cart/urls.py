from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    # normal pages if you want to keep them
    # path("", views.cart_detail, name="cart_detail"),

    # AJAX APIs
    path("ajax/add/<int:product_id>/", views.ajax_cart_add, name="ajax_cart_add"),
    path("ajax/detail/", views.ajax_cart_detail, name="ajax_cart_detail"),
    path("ajax/update/<int:item_id>/", views.ajax_cart_update, name="ajax_cart_update"),
    path("ajax/remove/<int:item_id>/", views.ajax_cart_remove, name="ajax_cart_remove"),
]
