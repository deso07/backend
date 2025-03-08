from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    path('', views.create_reservation, name='create_reservation'),
    path('<int:id>/', views.reservation_detail, name='reservation_detail'),
    path('user/<int:user_id>/', views.user_reservations, name='user_reservations'),
    path('<int:id>/update/', views.update_reservation_status, name='update_reservation_status'),
    path('<int:id>/delete/', views.delete_reservation, name='delete_reservation'),
]
=======
from .views import reservation_list, add_reservation, edit_reservation, delete_reservation

urlpatterns = [
    path('', reservation_list, name='reservations_list'),
    path('add/', add_reservation, name='add_reservation'),
    path('edit/<int:id>/', edit_reservation, name='edit_reservation'),
    path('delete/<int:id>/', delete_reservation, name='delete_reservation'),  # ✅ Убедись, что здесь <int:id>
]
>>>>>>> bddae2e57bd51d9b3a5c0d1ac075d0ae8df1698d
