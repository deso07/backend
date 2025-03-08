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