from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),  # Список заметок
    path('<int:pk>/', views.note_detail, name='note_detail'),  # Детали заметки
    path('create/', views.note_create, name='note_create'),  # Создание заметки
    path('<int:pk>/update/', views.note_update, name='note_update'),  # Редактирование заметки
    path('<int:pk>/delete/', views.note_delete, name='note_delete'),  # Удаление заметки
]