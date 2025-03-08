from django.shortcuts import render, get_object_or_404, redirect
from .models import Todolist, Todo
from .forms import TodolistForm, TodoForm

def index(request):
    return redirect('todo_lists')

def todo_lists(request):
    if request.method == 'POST':
        form = TodolistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_lists')
    else:
        form = TodolistForm()

    todo_lists = Todolist.objects.all()
    return render(request, 'todos/todo_lists.html', {'todo_lists': todo_lists, 'form': form})

def todo_list_detail(request, pk):
    todo_list = get_object_or_404(Todolist, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_list = todo_list
            todo.save()
            return redirect('todo_list_detail', pk=pk)
    else:
        form = TodoForm()

    return render(request, 'todos/todo_list_detail.html', {'todo_list': todo_list, 'form': form})

def todo_list_delete(request, pk):
    todo_list = get_object_or_404(Todolist, pk=pk)
    todo_list.delete()
    return redirect('todo_lists')

def todo_list_edit(request, pk):
    todo_list = get_object_or_404(Todolist, pk=pk)
    if request.method == 'POST':
        form = TodolistForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect('todo_lists')
    else:
        form = TodolistForm(instance=todo_list)

    return render(request, 'todos/todo_list_edit.html', {'form': form})

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo_list_pk = todo.todo_list.pk
    todo.delete()
    return redirect('todo_list_detail', pk=todo_list_pk)

def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', pk=todo.todo_list.pk)
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todos/todo_edit.html', {'form': form})