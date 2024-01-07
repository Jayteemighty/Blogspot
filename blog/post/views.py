from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    all_posts = Post.objects.all()
    posts_per_page = 10
    paginator = Paginator(all_posts, posts_per_page)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'posts': posts})

def about(request):
    posts = Post.objects.all()
    return render(request, 'about.html', {'posts':posts})

def contact(request):
    posts = Post.objects.all()
    return render(request, 'contact.html', {'posts':posts})

def post(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts':posts})

def category_posts(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, 'category_posts.html', {'category': category, 'posts': posts})