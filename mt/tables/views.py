from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Table
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_table(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        table = Table.objects.create(
            number=data['number'],
            seats=data['seats'],
            is_available=data.get('is_available', True)
        )
        return JsonResponse({'id': table.id, 'number': table.number, 'seats': table.seats, 'is_available': table.is_available}, status=201)

def table_list(request):
    tables = Table.objects.all()
    return JsonResponse(list(tables.values()), safe=False)

def available_tables(request):
    available_tables = Table.objects.filter(is_available=True)
    return JsonResponse(list(available_tables.values()), safe=False)