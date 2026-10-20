"""Представления приложения блога."""

from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post


def published_posts():
    """Возвращает опубликованные публикации с наступившей датой."""
    return Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    ).select_related('author', 'location', 'category')


def index(request):
    """Отображает главную страницу со свежими публикациями."""
    post_list = published_posts()[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def category_posts(request, category_slug):
    """Отображает публикации выбранной категории."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = published_posts().filter(category=category)
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)


def post_detail(request, post_id):
    """Отображает страницу отдельной публикации."""
    post = get_object_or_404(
        published_posts(),
        pk=post_id,
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)
