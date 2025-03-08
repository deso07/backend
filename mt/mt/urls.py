from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
=======
from django.shortcuts import redirect
>>>>>>> bddae2e57bd51d9b3a5c0d1ac075d0ae8df1698d

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
<<<<<<< HEAD
]
=======
    path('tables/', include('tables.urls')),
    path('reservations/', include('reservations.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Встроенные маршруты Django
    path('', lambda request: redirect('/accounts/login/')),  # Перенаправление на страницу логина
]
>>>>>>> bddae2e57bd51d9b3a5c0d1ac075d0ae8df1698d
