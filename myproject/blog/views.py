from django.http import HttpResponse, Http404

CATEGORIES = {
    1: "Чилл территории Python",
    2: "Django, сложно, но можно!",
    3: "Flask, бегите, глупцы!",
}

def blog_catalog(request):
    return HttpResponse("Тут будет блог")

def category_list(request):
    categories = ", ".join([str(key) for key in CATEGORIES.keys()])
    return HttpResponse(f"Список категорий: {categories}")

def category_detail(request, category_id):
    if category_id not in CATEGORIES:
        raise Http404
    return HttpResponse(f"Категория {category_id} - {CATEGORIES[category_id]}")