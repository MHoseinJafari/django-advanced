from django.urls import path
from . import views
from .views import TaskListView, TaskCreateView, TaskDetailView, TaskEditView, TaskDeleteView

app_name = "tasks"

urlpatterns = [
    path('task/', views.TaskListView.as_view(), name= "task-list"),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name= "task-detail"),
    path('task/create/', views.TaskCreateView.as_view(), name= "task-create"),
    path('task/<int:pk>/edit/', views.TaskEditView.as_view(), name= "task-edit"),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name="task-delete")
]
