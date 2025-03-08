from django.test import TestCase
from .models import Table

class TableModelTest(TestCase):

    def setUp(self):
        Table.objects.create(number=1, seats=4, is_available=True)
        Table.objects.create(number=2, seats=2, is_available=False)

    def test_table_creation(self):
        table = Table.objects.get(number=1)
        self.assertEqual(table.seats, 4)
        self.assertTrue(table.is_available)

    def test_table_availability(self):
        table = Table.objects.get(number=2)
        self.assertFalse(table.is_available)

    def test_unique_table_number(self):
        with self.assertRaises(Exception):
            Table.objects.create(number=1, seats=6, is_available=True)