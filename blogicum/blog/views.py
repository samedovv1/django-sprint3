from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post


POSTS_ON_MAIN_PAGE = 5


def get_published_posts():
    """Получить опубликованные записи с доступной категорией."""
    return Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    ).select_related('author', 'category', 'location')


def index(request):
    """Отобразить пять последних опубликованных записей."""
    context = {'post_list': get_published_posts()[:POSTS_ON_MAIN_PAGE]}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    """Отобразить отдельную публикацию или вернуть ошибку 404."""
    post = get_object_or_404(get_published_posts(), pk=id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    """Отобразить опубликованные записи выбранной категории."""
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True,
    )
    context = {
        'category': category,
        'post_list': get_published_posts().filter(category=category),
    }
    return render(request, 'blog/category.html', context)
