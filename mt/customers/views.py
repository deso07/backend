from django.shortcuts import render
from django.http import JsonResponse
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all()
    data = list(customers.values())
    return JsonResponse(data, safe=False)

def customer_detail(request, id):
    customer = Customer.objects.get(id=id)
    return JsonResponse({'name': customer.name, 'phone': customer.phone})