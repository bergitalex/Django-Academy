from django.shortcuts import render, get_object_or_404

from .models import Post, Category, Tag

menu = [
    {
        "name": "Главная",
        "url": "/",
        "alias": "main"
    },
    {
        "name": "Блог",
        "url": "/blog/",
        "alias": "blog"
    },
    {
        "name": "О проекте",
        "url": "/about/",
        "alias": "about"
    }
]

def main(request):
    context = {
        'menu': menu,
    }
    print(context.values())
    return render(request, 'main.html', context)

def about(request):
    context = {
        'menu': menu,
        'user_count': 100,  # Пример использования переменной
    }
    return render(request, 'about.html', context)

def blog(request):
    context = {
        'menu': menu,
        'posts': Post.objects.all(),
    }
    return render(request, 'blog.html', context)

def post_list(request):
    """Представление, которое возвращает список всех постов."""
    posts = Post.objects.all()
    context = {
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'blog.html', context)

def post_detail(request, slug):
    """Представление, которое возвращает конкретный пост по slug."""
    post = get_object_or_404(Post, slug=slug)
    context = {
        'menu': menu,
        'post': post,
    }
    print(post.tags)
    return render(request, 'post_detail.html', context)