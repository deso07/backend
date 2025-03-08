from django.test import TestCase
from .models import Customer

class CustomerModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(name="John Doe", phone="1234567890")

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.phone, "1234567890")

    def test_customer_str(self):
        self.assertEqual(str(self.customer), "John Doe")  # Assuming you have a __str__ method in your model