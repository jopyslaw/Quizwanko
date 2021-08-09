"""Quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path, include
from first.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('category', category, name='category'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('category/select_category/<id>', select_category, name='select_category'),
    path('check_answers', check_answers, name='check_answers'),
    path('author', author, name='author'),
    path('contact', contact, name='contact'),
    path('random', random, name='random'),
    path('random/check_answers', check_answers_random, name='check_answers_random'),
    path('leaderboard', leaderboard, name="leaderboard"),
]
