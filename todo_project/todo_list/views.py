from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.http import Http404

# todo/views.py

from django.shortcuts import render
from .models import Task

def task_list(request):
    """
    Displays a list of all tasks with a calculated animation delay.
    """
    tasks = Task.objects.all()

    # Create a new list with animation delays
    tasks_with_delay = []
    for index, task in enumerate(tasks):
        delay = index * 0.1
        tasks_with_delay.append({
            'task': task,
            'delay': delay
        })

    # Pass the new list to the template
    return render(request, 'todo/task_list.html', {'tasks': tasks_with_delay})

def task_detail(request, pk):
    """
    Displays the details of a single task.
    Handles a custom 404 error if the task is not found.
    """
    try:
        task = get_object_or_404(Task, pk=pk)
    except Http404:
        return render(request, '404.html', {'message': 'Task not found.'}, status=404)
    return render(request, 'todo/task_detail.html', {'task': task})

def add_task(request):
    """
    Handles adding a new task.
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
            return redirect('task_list')
    return render(request, 'todo/add_task.html')

def update_task(request, pk):
    """
    Handles updating an existing task.
    """
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        completed = request.POST.get('completed') == 'on'
        if title:
            task.title = title
            task.completed = completed
            task.save()
            return redirect('task_list')
    return render(request, 'todo/update_task.html', {'task': task})

def delete_task(request, pk):
    """
    Handles deleting a task.
    """
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/confirm_delete.html', {'task': task})
