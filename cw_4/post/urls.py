from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('threads/', views.thread_list, name='threads'),
    path('threads/<int:pk>/', views.thread_detail, name='thread_detail'),
    path('threads/<int:pk>/delete/', views.thread_delete, name='thread_delete'),
    path('threads/<int:pk>/edit/', views.thread_edit, name='thread_edit'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('posts/<int:pk>/edit/', views.post_edit, name='post_edit'),
]