from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/my/', views.my_posts, name='my_posts'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<int:id>/delete/', views.post_delete, name='post_delete'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
]