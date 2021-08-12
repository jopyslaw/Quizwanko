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
    path('login/check_login', check_login, name="check_login"),
    path('login/logout', logout, name="logout"),
    path('register/register_user', register_user, name="register_user"),
    path('login/edit_account', edit_account, name="edit_account"),
    path('login/edit_account/change_user_data', change_user_data, name="change_user_data"),
    path('login/edit_account/change_user_password', change_user_password, name="change_user_password"),
    path('login/edit_account/delete_account', delete_account, name="delete_account"),
    path('login/add_question', add_question, name="add_question"),
    path('login/add_question/add', add_this, name="add_this"),
    path('login/user_points', user_points, name="user_points"),
    path('login/check_questions', check_questions, name="check_questions"),
    path('login/check_questions/<id>', edit_question, name="edit_question"),
    path('login/accept_question', accept_question, name="accept_question"),
]
