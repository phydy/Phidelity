from django.shortcuts import render
from .models import Post, CHOICES

# Create your views here.
def blog_home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def forex_posts(request):
    context ={
        'posts' : Post.objects.filter(category="fx")
    }
    return render(request, 'blog/forex.html', context)

def crypto_posts(request):
    context ={
        'posts' : Post.objects.filter(category="bc")
    }
    return render(request, 'blog/crypto.html', context)

def indices_posts(request):
    context ={
        'posts' : Post.objects.filter(category="ix")
    }
    return render(request, 'blog/indices.html', context)

def commodities_posts(request):
    context ={
        'posts' : Post.objects.filter(category="cm")
    }
    return render(request, 'blog/commodities.html', context)

def edu_posts(request):
    context ={
        'posts' : Post.objects.filter(category="ed")
    }
    return render(request, 'blog/edu.html', context)
