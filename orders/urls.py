from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("", views.order_list, name="order_list"),  
    path("<int:order_id>/", views.order_detail, name="order_detail"),  
    path("<int:order_id>/update-status/", views.update_order_status, name="update_order_status"),  
    path("history/", views.order_history, name="order_history"),  # ✅ new route added
]
