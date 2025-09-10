from django.shortcuts import render
from to_do.models import Task

def home(req):
    tasks=Task.objects.filter(is_completed=False).order_by('-is_updated')


    completed_tasks=Task.objects.filter(is_completed=True)
    context={'tasks':tasks, 
             'is_completed':completed_tasks,}

    return render(req,'to_do.html',context) 