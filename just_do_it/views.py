from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Rubric, Target, Task
from django.contrib.auth.models import User
# Create your views here.
import datetime


def index(request):
    tasks = Task.objects.filter(target__isnull=True).filter(finish_date__gte=datetime.date.today()).exclude(complete=True)
    targets = Target.objects.filter(finish_date__gte=datetime.date.today()).exclude(complete=True)
    print(request.user)
    return render(request, 'just_do_it/index.html', {'tasks': tasks, 'targets': targets})


def target_processing(request, target_id):
    target = Target.objects.get(id=target_id)
    post_values = request.POST.keys()
    #TODO сделать одним запросом к бд?
    for key in post_values:
        try:
            task = target.task_set.get(id=key)
            task.complete = True
            task.save()
        except:
            pass
    #проверка что все задачи выполнены
    tasks = target.task_set.all()
    counter = 0
    for task in tasks:
        if task.complete == True:
            counter += 1
    if counter == len(tasks):
        target.complete = True
        target.save()
    return redirect(reverse('index'))


def target_archive(request):
    targets = Target.objects.filter(finish_date__lt=datetime.date.today())
    return render(request, 'just_do_it/target_archive.html', {'targets': targets})