from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
    path('catalog/', views.blog_catalog, name='blog_catalog'),
]
