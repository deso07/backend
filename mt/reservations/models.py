from django.db import models
<<<<<<< HEAD

class Reservation(models.Model):
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    table = models.ForeignKey('tables.Table', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[
            ("pending", "Pending"),
            ("confirmed", "Confirmed"),
            ("canceled", "Canceled")
        ],
        default="pending"
    )

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return f"{self.customer.name} - Table {self.table.number}"
=======
from django.core.exceptions import ValidationError
from tables.models import Table
from customers.models import Customer

class Reservation(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("canceled", "Canceled"),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    def clean(self):
        """Проверяем перед сохранением, не занят ли столик и нет ли у пользователя уже брони"""
        if Reservation.objects.filter(table=self.table, date=self.date).exclude(id=self.id).exists():
            raise ValidationError(f"Table {self.table.number} is already booked on {self.date}")

        if Reservation.objects.filter(customer=self.customer, date=self.date).exclude(id=self.id).exists():
            raise ValidationError(f"Customer {self.customer.name} already has a reservation on {self.date}")

    def save(self, *args, **kwargs):
        """Запускаем валидацию перед сохранением"""
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer.name} - Table {self.table.number} ({self.date})"
>>>>>>> bddae2e57bd51d9b3a5c0d1ac075d0ae8df1698d
