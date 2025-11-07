from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'category', 'image', 'content', 'tags', 'is_published']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 6, 'class': 'form-control'}),
        }
