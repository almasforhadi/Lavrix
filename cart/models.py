from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
from django.utils import timezone

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_items", null=True, blank=True)
    session_key = models.CharField(max_length=40, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    # models.py, inside CartItem
    def total_price(self):
        # Use sale_price if available, else regular price
        price = self.product.sale_price if self.product.sale_price else self.product.price
        return price * self.quantity

