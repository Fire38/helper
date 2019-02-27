from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

import datetime

from .forms import RegisterForm, LoginForm
from .models import Target, Task


# Create your views here.
def index(request):
    login_form = LoginForm()
    tasks = Task.objects.filter(target__isnull=True).filter(finish_date__gte=datetime.date.today()).exclude(complete=True)
    targets = Target.objects.filter(finish_date__gte=datetime.date.today()).exclude(complete=True)
    print(request.user.username)
    return render(request, 'just_do_it/index.html', {'tasks': tasks, 'targets': targets, 'form': login_form})


def target_processing(request, target_id):
    target = Target.objects.get(id=target_id)
    post_values = request.POST.keys()
    # TODO сделать одним запросом к бд?
    for key in post_values:
        try:
            task = target.task_set.get(id=key)
            task.complete = True
            task.save()
        except:
            pass
    # проверка что все задачи выполнены
    tasks = target.task_set.all()
    counter = 0
    for task in tasks:
        if task.complete is True:
            counter += 1
    if counter == len(tasks):
        target.complete = True
        target.save()
    return redirect(reverse('index'))


def target_archive(request):
    targets = Target.objects.filter(finish_date__lt=datetime.date.today())
    return render(request, 'just_do_it/target_archive.html', {'targets': targets})


def login_user(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect(reverse('index'))
        else:
            return redirect(reverse('index'))


def logout_user(request):
    logout(request)
    return redirect(reverse('index'))


def register(request):
    if request.method == 'POST':
        print(request.POST)
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.set_password(request.POST['password'])
            user.save()
            auth_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if auth_user is not None:
                login(request, auth_user)
                return redirect(reverse('index'))
    else:
        register_form = RegisterForm()

    return render(request, 'just_do_it/register.html', {'form': register_form})
