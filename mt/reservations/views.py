<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Reservation
from customers.models import Customer
from tables.models import Table
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone

@csrf_exempt
def create_reservation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        customer_id = data.get('customer_id')
        table_id = data.get('table_id')
        date = data.get('date')

        # Check if the customer already has a reservation for that date
        if Reservation.objects.filter(customer_id=customer_id, date=date).exists():
            return JsonResponse({'error': 'Customer already has a reservation for this date.'}, status=400)

        # Check if the table is already reserved
        if Reservation.objects.filter(table_id=table_id, date=date).exists():
            return JsonResponse({'error': 'Table is already reserved for this date.'}, status=400)

        customer = get_object_or_404(Customer, id=customer_id)
        table = get_object_or_404(Table, id=table_id)

        reservation = Reservation.objects.create(customer=customer, table=table, date=date, status='pending')
        return JsonResponse({'id': reservation.id}, status=201)

def reservation_detail(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    return JsonResponse({
        'customer': reservation.customer.name,
        'table': reservation.table.number,
        'date': reservation.date,
        'status': reservation.status
    })

def user_reservations(request, user_id):
    reservations = Reservation.objects.filter(customer_id=user_id)
    return JsonResponse(list(reservations.values()), safe=False)

@csrf_exempt
def update_reservation_status(request, id):
    if request.method == 'POST':
        data = json.loads(request.body)
        status = data.get('status')

        reservation = get_object_or_404(Reservation, id=id)
        reservation.status = status
        reservation.save()
        return JsonResponse({'message': 'Reservation status updated successfully.'})

@csrf_exempt
def delete_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    reservation.delete()
    return JsonResponse({'message': 'Reservation deleted successfully.'})
=======

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Reservation
from tables.models import Table
import json


def create_reservation(request):
    if request.method == "POST":
        data = json.loads(request.body)
        customer_id = data["customer_id"]
        table_id = data["table_id"]
        date = data["date"]

        # ❌ Проверка 1: Столик уже забронирован на эту дату
        existing_reservation = Reservation.objects.filter(table_id=table_id, date=date).exists()
        if existing_reservation:
            return JsonResponse({"error": "Table is already booked on this date"}, status=400)

        # ❌ Проверка 2: У пользователя уже есть бронь на этот день
        user_existing_reservation = Reservation.objects.filter(customer_id=customer_id, date=date).exists()
        if user_existing_reservation:
            return JsonResponse({"error": "You already have a reservation on this date"}, status=400)

        # ✅ Создаём бронь
        reservation = Reservation.objects.create(customer_id=customer_id, table_id=table_id, date=date, status="confirmed")

        # ❌ Обновляем `is_available = False`
        table = Table.objects.get(id=table_id)
        table.is_available = False
        table.save()

        return JsonResponse({
            "id": reservation.id,
            "customer": reservation.customer.name,
            "table": f"Table {reservation.table.number}",
            "date": reservation.date,
            "status": reservation.status
        })

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/reservations_list.html', {'reservations': reservations})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation


# 📌 Удаление бронирования
def delete_reservation(request, id):  # ✅ Принимаем `id` как аргумент
    reservation = get_object_or_404(Reservation, id=id)

    if request.method == "POST":
        reservation.delete()
        return redirect('reservations_list')

    return render(request, 'reservations/delete_reservation.html', {'reservation': reservation})


# 📌 Добавление брони
def add_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservations_list')
    else:
        form = ReservationForm()
    return render(request, 'reservations/add_reservation.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm

# 📌 Редактирование бронирования
def edit_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservations_list')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservations/edit_reservation.html', {'form': form, 'reservation': reservation})
>>>>>>> bddae2e57bd51d9b3a5c0d1ac075d0ae8df1698d
