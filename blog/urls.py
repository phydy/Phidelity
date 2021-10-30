from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog-home'),
    path('forex/', views.forex_posts, name='forex-blog'),
    path('edu/', views.edu_posts, name='edu-blog'),
    path('crypto/', views.crypto_posts, name='crypto-blog'),
    path('indices/', views.indices_posts, name='crypto-blog'),
    path('commodities/', views.commodities_posts, name='commodities-blog')
]