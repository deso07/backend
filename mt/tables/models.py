from django.db import models

class Table(models.Model):
    number = models.IntegerField(verbose_name='Номер стола')
    seats = models.IntegerField(verbose_name='Количество мест')
    is_available = models.BooleanField(verbose_name='Доступен', default=True)

    class Meta:
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'

    def __str__(self):
        return f"Стол №{self.number}"
