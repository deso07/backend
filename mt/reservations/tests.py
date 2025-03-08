from django.test import TestCase
<<<<<<< HEAD
from .models import Reservation
from customers.models import Customer
from tables.models import Table
from django.utils import timezone

class ReservationModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(name="John Doe", phone="1234567890")
        self.table = Table.objects.create(number=1, seats=4, is_available=True)
        self.reservation = Reservation.objects.create(
            customer=self.customer,
            table=self.table,
            date=timezone.now().date(),
            status="pending"
        )

    def test_reservation_creation(self):
        self.assertEqual(self.reservation.customer.name, "John Doe")
        self.assertEqual(self.reservation.table.number, 1)
        self.assertEqual(self.reservation.status, "pending")

    def test_reservation_str(self):
        self.assertEqual(str(self.reservation), f'Reservation for {self.customer.name} on {self.reservation.date}')
=======

# Create your tests here.
>>>>>>> bddae2e57bd51d9b3a5c0d1ac075d0ae8df1698d
