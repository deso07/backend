from django.test import TestCase
<<<<<<< HEAD
from .models import Customer

class CustomerModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(name="John Doe", phone="1234567890")

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.phone, "1234567890")

    def test_customer_str(self):
        self.assertEqual(str(self.customer), "John Doe")  # Assuming you have a __str__ method in your model
=======

# Create your tests here.
>>>>>>> bddae2e57bd51d9b3a5c0d1ac075d0ae8df1698d
