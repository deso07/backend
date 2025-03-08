from django.db import models

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