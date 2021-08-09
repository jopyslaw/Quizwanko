from django.shortcuts import redirect, render
from .models import Category, LeaderBoard, Question
from random import choice
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.contrib.auth import logout as logout_auth

# Create your views here.

def main(request):
    leaders = LeaderBoard.objects.all().values().order_by('-points')[:10]
    data = {'leaders': leaders}
    return render(request,"first/index.html", data)

def category(request):
    category = Category.objects.all().exclude(category__iexact = 'Random')
    data = {'category':category}
    return render(request, "first/category.html", data)

def login(request):
    return render(request, "first/login.html")

def register(request):
    return render(request, "first/register.html")

def select_category(request, id): 
    category = Category.objects.get(pk=id)
    questions = Question.objects.all().filter(category=category)
    data = {'questions':questions, 'category': category}
    return render(request, "first/quiz.html", data)


def check_answers(request):
    pkt = 0
    data = request.GET
    print(data)
    category = Category.objects.get(category=data['category'])
    id_cat = category.id
    good_answer = Question.objects.values().filter(category_id=id_cat)
    new_data = data.dict()
    for i in good_answer:
        key = i['id']
        send_answer = new_data[str(key)]
        if send_answer == i['good_answer']:
            pkt += 1
        else:
            pkt += 0
    question_len = len(new_data)-1
    points = {'points': pkt, 'question_counter': question_len, 'category':category}
    return render(request, "first/answers.html", points)


def author(request):
    return render(request, "first/author.html")


def contact(request):
    return render(request, "first/contact.html")

def random(request): #Wyświetla 10 randomowych pytań z bazy danych
    category = Category.objects.get(category="Random")
    all_questions = Question.objects.all().values()
    new_list = []
    i = 0
    while i < 5:
        check = choice(all_questions)
        if check in new_list:
            continue
        else:
            new_list.append(check)
            i += 1
    data = { 'questions': new_list, 'category':category}
    return render(request, "first/random.html", data)


def leaderboard(request):
    data = request.POST
    category = Category.objects.get(category=data['category'])
    username = data['username']
    points = data['points']
    person = LeaderBoard(category=category, username=username, points=points)
    person.save()
    return redirect('main')

def check_answers_random(request):
    pkt = 0
    category = Category.objects.get(category="Random")
    data = request.GET
    new_data = data.dict()
    new_data.pop('category')
    for i in new_data.keys():
        question = Question.objects.values('good_answer').get(id=i)
        if question['good_answer'] == new_data[f'{i}']:
            pkt += 1
        else:
            pkt += 0
    len_data = len(new_data)
    points = {'points': pkt, 'question_counter': len_data, 'category':category}
    return render(request, "first/answers.html", points)


def check_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login_auth(request, user)
        return redirect('main')
    else:
        data = {'error': 'Nieprawidłowe hasło lub login'}
        return render(request, "first/login.html", data)


def logout(request):
    logout_auth(request)
    return redirect('main')
