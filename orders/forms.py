from django import forms
from .models import Order,Product

class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["status"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3, "placeholder": "Enter product details"}),
        }
