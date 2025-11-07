from django.shortcuts import render, get_object_or_404
from .models import BlogPost, BlogCategory


def blog_list(request, category_slug=None):
    categories = BlogCategory.objects.all().order_by('name')
    active_category = None
    posts = BlogPost.objects.filter(is_published=True).select_related('author', 'category').order_by('-created_at')

    if category_slug:
        active_category = get_object_or_404(BlogCategory, slug=category_slug)
        posts = posts.filter(category=active_category)

    context = {
        'categories': categories,
        'posts': posts,
        'active_category': active_category,
        'page_title': active_category.name if active_category else "All Blog Posts",
    }
    return render(request, 'blog_list.html', context)




def blog_detail(request, slug):
    post = get_object_or_404(BlogPost.objects.select_related('author', 'category'), slug=slug, is_published=True)
    related_posts = BlogPost.objects.filter(category=post.category, is_published=True).exclude(id=post.id)[:3]

    context = {
        'post': post,
        'related_posts': related_posts,
        'page_title': post.title,
    }
    return render(request, 'blog_detail.html', context)
