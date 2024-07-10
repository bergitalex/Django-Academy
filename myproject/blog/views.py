from django.shortcuts import render

# Пример данных
posts = [
    {
        "category": "Python",
        "tags": ["основы", "синтаксис", "советы"],
        "slug": "introduction-to-python",
        "title": "Введение в Python",
        "text": ("Python — это высокоуровневый язык программирования с простым синтаксисом и мощными библиотеками. "
                 "Он широко используется для разработки веб-приложений, анализа данных, научных исследований и автоматизации задач. "
                 "Благодаря своей универсальности и поддержке сообщества, Python стал одним из самых популярных языков программирования в мире. "
                 "Кроме того, наличие множества онлайн-курсов и документации делает его отличным выбором для начинающих. "
                 "В этой статье мы рассмотрим основные концепции и примеры использования Python."),
        "author": "Иван Петров",
        "published_date": "2024-06-25",
        "comments": [
            {"author": "Алексей Смирнов", "text": "Отличная статья для новичков!", "date": "2024-06-26"},
            {"author": "Мария Иванова", "text": "Python действительно лучший выбор для начинающих.", "date": "2024-06-27"}
        ]
    }
]

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
        'posts': posts,
    }
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
        'posts': posts,
    }
    return render(request, 'blog.html', context)

def post_detail(request, slug):
    post = next(post for post in posts if post["slug"] == slug)
    context = {
        'menu': menu,
        'post': post,
    }
    return render(request, 'post_detail.html', context)
