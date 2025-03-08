from django import forms
from .models import Table

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['number', 'seats', 'is_available']
        labels = {
            'number': 'Номер стола',
            'seats': 'Количество мест',
            'is_available': 'Доступен'
        }
