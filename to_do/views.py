from django.shortcuts import render,redirect,get_object_or_404
from .models import Task

def addTask(req):
    task=req.POST['task']
    Task.objects.create(task=task)

    return redirect('home')


def mark_as_done(req,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=True

    task.save()

    return redirect('home')


def delete(req,pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()

    return redirect('home')


def mark_as_undone(req,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=False

    task.save()

    return redirect('home')



def edit_task(request,pk):
    get_task=get_object_or_404(Task,pk=pk)


    if request.method=='POST':
        new_task=get_object_or_404(Task,pk=pk)
        new_task=request.POST.get('task')
        print(new_task)
        get_task.task=new_task
        get_task.save()
        return redirect('home')



    
    else:
        context={'get_task':get_task}
        return render(request,'edit.html',context)
