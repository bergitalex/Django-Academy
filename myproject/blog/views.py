from django.shortcuts import render, get_object_or_404
from django.db.models import F
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
        "name": "Поисковик",
        "url": "/catalog/",
        "alias": "blog-catalof"
    },
    {
        "name": "О проекте",
        "url": "/about/",
        "alias": "about"
    },
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

def blog_catalog(request):
    """
    Вьюшка для страницы "Блог" с каталогом постов.
    """
    if request.method == "GET":
        search = request.GET.get("search")
        search_in_title = request.GET.get("searchInTitle")
        search_in_text = request.GET.get("searchInText")
        search_in_tags = request.GET.get("searchInTags")

        posts_filtered = Post.objects.all()

        if search:
            if not search_in_title and not search_in_text and not search_in_tags:
                posts_filtered = posts_filtered.filter(text__icontains=search)
            if search_in_title:
                posts_filtered = posts_filtered.filter(title__icontains=search)
            if search_in_text:
                posts_filtered = posts_filtered.filter(text__icontains=search)
            if search_in_tags:
                posts_filtered = posts_filtered.filter(tags__name__icontains=search)

        context = {
            "posts": posts_filtered,
        }
        return render(request, "blog_catalog.html", context)

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
    Post.objects.filter(pk=post.pk).update(views=F('views') + 1)
    post.refresh_from_db()
    context = {
        'menu': menu,
        'post': post,
    }
    return render(request, 'post_detail.html', context)