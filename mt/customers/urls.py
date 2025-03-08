from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
]
=======
from .views import customer_list, customer_detail
from django.urls import path
from .views import customer_list, add_customer, edit_customer, delete_customer


urlpatterns = [
    path('', customer_list, name='customers_list'),  # <-- Здесь должен быть name='customers_list'
    path('<int:id>/', customer_detail, name='customer_detail'),
    path('add/', add_customer, name='add_customer'),
    path('edit/<int:id>/', edit_customer, name='edit_customer'),
    path('delete/<int:id>/', delete_customer, name='delete_customer'),
]


>>>>>>> bddae2e57bd51d9b3a5c0d1ac075d0ae8df1698d
