from django.urls import path
from . import views

app_name = 'todos'  # This defines the namespace

urlpatterns = [
    path('', views.todo_list, name='index'),
    path('<int:id>/', views.todo_detail, name='detail'),
    path('create/', views.todo_create, name='create'),
    path('<int:id>/delete/', views.todo_delete, name='delete'),
]