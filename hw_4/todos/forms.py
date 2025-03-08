from django import forms
from .models import Todolist, Todo

class TodolistForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['title', 'description']

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'status']