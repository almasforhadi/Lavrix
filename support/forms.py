from django import forms
from .models import SupportTicket, SupportResponse

class SupportTicketForm(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = ['subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        }

class SupportResponseForm(forms.ModelForm):
    class Meta:
        model = SupportResponse
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
