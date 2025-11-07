from django import forms
from .models import CartItem

class CartAddForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ["quantity"]
