from django.db import models

class Table(models.Model):
<<<<<<< HEAD
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Table'
        verbose_name_plural = 'Tables'

    def __str__(self):
        return f"Table {self.number}"
=======
    number = models.IntegerField(verbose_name='Номер стола')
    seats = models.IntegerField(verbose_name='Количество мест')
    is_available = models.BooleanField(verbose_name='Доступен', default=True)

    class Meta:
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'

    def __str__(self):
        return f"Стол №{self.number}"
>>>>>>> bddae2e57bd51d9b3a5c0d1ac075d0ae8df1698d
