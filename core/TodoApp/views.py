from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskListView(LoginRequiredMixin,ListView):
    model = Task

class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    
class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['name', 'status']
    success_url = '/TodoApp/task/'

class TaskEditView(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ["name", "status"]
    success_url = '/TodoApp/task/'

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    success_url = '/TodoApp/task/'