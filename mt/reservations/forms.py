from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer', 'table', 'date', 'status']
        labels = {
            'customer': 'Клиент',
            'table': 'Столик',
            'date': 'Дата',
            'status': 'Статус'
        }