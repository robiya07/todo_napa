from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils import timezone

from todo.forms import TaskCreateModelForm, TaskUpdateModelForm
from todo.models import TaskModel


@login_required
def task_create_view(request):
    form = TaskCreateModelForm()
    if request.method == 'POST':
        form = TaskCreateModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    context = {
        'create_form': form
    }
    return render(request, 'main/task_create.html', context)


@login_required
def task_list_view(request):
    search = request.GET.get('search', '')
    if search:
        tasks = TaskModel.objects.filter(Q(name__icontains=search) | Q(description__icontains=search))
    else:
        tasks = TaskModel.objects.all()
    context = {
        'tasks': tasks,
        'search': search
    }
    return render(request, 'main/task_list.html', context)


@login_required
def task_update_view(request, pk):
    task = TaskModel.objects.get(id=pk)
    form = TaskUpdateModelForm(instance=task)
    if request.method == 'POST':
        form = TaskUpdateModelForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    context = {
        'update_form': form,
        'task': task
    }
    return render(request, 'main/task_update.html', context)


@login_required
def task_delete_view(request, pk):
    task = TaskModel.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'main/task_delete.html')


@login_required
def task_detail_view(request, pk):
    task = TaskModel.objects.get(id=pk)
    diff = timezone.now() - task.created_at
    ago = ""
    if diff.days:
        if diff.days > 365:
            ago = f"{diff.days // 365} year ago" if diff.days // 365 == 1 else f"{diff.days // 365} years ago"
        elif diff.days > 30:
            ago = f"{diff.days // 30} month ago" if diff.days // 30 == 1 else f"{diff.days // 30} months ago"
        else:
            ago = f"{diff.days} day ago" if diff.days // 30 == 1 else f"{diff.days} days ago"
    elif m := (diff.seconds // 60):
        if m // 60 > 1:
            ago = f"{m // 60} hour ago" if m // 60 == 1 else f"{m // 60} hours ago"
        else:
            ago = f"{m % 60} minute ago" if m % 60 == 1 else f"{m % 60} minutes ago"
    else:
        ago = "just now"

    context = {
        'task': task,
        'ago': ago
    }
    return render(request, 'main/task_detail.html', context)
