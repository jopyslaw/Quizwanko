from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Category, Questions
from random import choice

# Create your views here.

def main(request):
    return render(request,"first/index.html")

def category(request):
    category = Category.objects.all()
    data = {'category':category}
    return render(request, "first/category.html", data)

def login(request):
    return render(request, "first/login.html")

def register(request):
    return render(request, "first/register.html")

def select_category(request, id): 
    category = Category.objects.get(pk=id)
    questions = Questions.objects.all().filter(category=category)
    data = {'questions':questions, 'category': category}
    return render(request, "first/quiz.html", data)


def check_answers(request):
    pkt = 0
    data = request.POST
    category = Category.objects.get(category=data['category'])
    id_cat = category.id
    good_answer = Questions.objects.values().filter(category_id=id_cat)
    new_data = data.dict()
    for i in good_answer:
        key = i['id']
        send_answer = new_data[str(key)]
        if send_answer == i['good_anwer']:
            pkt += 1
        else:
            pkt += 0
    points = {'points': pkt}
    return render(request, "first/answers.html", points)


def author(request):
    return render(request, "first/author.html")


def contact(request):
    return render(request, "first/contact.html")

def random(request): #Wyświetla 10 randomowych pytań z bazy danych
    all_questions = Questions.objects.all().values()
    new_list = []
    i = 0
    while i < 5:
        check = choice(all_questions)
        if check in new_list:
            continue
        else:
            new_list.append(check)
            i += 1
    data = { 'questions': new_list}
    return render(request, "first/random.html", data)


def check_answers_random(request):
    pkt = 0
    data = request.POST
    new_data = data.dict()
    new_data.pop('category')
    new_data.pop('csrfmiddlewaretoken')
    for i in new_data.keys():
        question = Questions.objects.values('good_anwer').get(id=i)
        if question['good_anwer'] == new_data[f'{i}']:
            pkt += 1
        else:
            pkt += 0
    points = {'points': pkt}
    return render(request, "first/answers.html", points)


