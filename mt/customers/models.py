from django.db import models

class Customer(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    class Meta:
        db_table = 'customers_customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.name
=======
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
>>>>>>> bddae2e57bd51d9b3a5c0d1ac075d0ae8df1698d
