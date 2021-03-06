from django.core.checks import messages
from django.shortcuts import redirect, render
from .models import Category, LeaderBoard, Question, Users_question
from random import choice
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.contrib.auth import logout as logout_auth
from django.contrib.auth.models import User
from django.contrib import messages

GROUPS_NAME = ['Moderators']

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
        messages.error(request, "Nie prawidłowe hasło lub nazwa użytkownika", extra_tags="login_status")
        return redirect('login')


def logout(request):
    logout_auth(request)
    return redirect('main')


def register_user(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Pomyślnie założono konto", extra_tags="register_status")
    except:
        messages.error(request, "Taki użytkownik już istnieje", extra_tags="register_status")
    return redirect('register')

def edit_account(request):
    return render(request, 'first/account.html')


def change_user_data(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    user = request.user
    if request.user.is_authenticated:
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        messages.success(request, "Profil został zaaktualizowany",extra_tags="profile_update")
        return redirect('edit_account')
    else:
        return redirect('login')
    


def change_user_password(request):
    old_password = request.POST['old_password']
    new_password = request.POST['new_password']
    user = request.user
    if user.is_authenticated:
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            messages.success(request, "Hasło zostało zmienione", extra_tags="change_password")
            return redirect('edit_account')
        else:
            messages.error(request, "Hasło nie zostało zmienione", extra_tags="change_password")
            return redirect('edit_account')
    else:
        return redirect('login')

def delete_account(request):
    choice = request.POST['delete_account']
    user = request.user
    if user.is_authenticated:
        if choice == 'true':
            user.delete()
            return redirect('main')


def add_question(request):
    category = Category.objects.all().exclude(category__iexact = 'Random')
    data = {'category':category}
    return render(request, "first/add_question.html", data)


def add_this(request):
    category = request.POST['category']
    question = request.POST['question_area']
    odp_a = request.POST['answer_a']
    odp_b = request.POST['answer_b']
    odp_c = request.POST['answer_c']
    odp_d = request.POST['answer_d']
    odp_good = request.POST['answer_good']
    category_data = Category.objects.get(category=category)
    question = Users_question(category=category_data, question=question, answer_a=odp_a, answer_b=odp_b, answer_c=odp_c, answer_d=odp_d, good_answer=odp_good)
    question.save()
    return redirect('add_question')


def user_points(request):
    username = request.user
    data = LeaderBoard.objects.filter(username=username)
    points_for_user = {'points':data}
    return render(request, 'first/user_info.html', points_for_user)


def check_questions(request):
    if request.user.groups.filter(name__in=GROUPS_NAME).exists():
        question = Users_question.objects.all()
        data = {'question':question}
        return render(request, 'first/check_questions.html', data)
    else:
        return redirect('main')


def edit_question(request, id):
    question = Users_question.objects.filter(pk=id).values()
    for c in question:
        category_id = c['category_id']
    category = Category.objects.all().exclude(pk = category_id)
    category.exclude(category__iexact="Random")
    print(category)
    question_category = Category.objects.filter(pk=category_id)
    data = {'question':question, 'category':category, 'question_category':question_category}
    return render(request, 'first/edit_question.html', data)


def accept_question(request):
    category = request.POST['category']
    question = request.POST['question_area']
    odp_a = request.POST['answer_a']
    odp_b = request.POST['answer_b']
    odp_c = request.POST['answer_c']
    odp_d = request.POST['answer_d']
    odp_good = request.POST['answer_good']
    category_data = Category.objects.get(category=category)
    question = Question(category=category_data, question=question, answer_a=odp_a, answer_b=odp_b, answer_c=odp_c, answer_d=odp_d, good_answer=odp_good)
    question.save()
    question_delete = Users_question.objects.get(question=question)
    question_delete.delete()
    return redirect('check_questions')

    

