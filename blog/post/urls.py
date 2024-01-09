from django.urls import path
from . import views
from .views import category_posts

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]