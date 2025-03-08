from django.contrib import admin
from .models import Reservation

<<<<<<< HEAD
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'table', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('customer__name', 'table__number')
=======
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'table', 'date', 'status')
    list_filter = ('date', 'status')
    search_fields = ('customer__name', 'table__number', 'date')

    def save_model(self, request, obj, form, change):
        """Вызываем валидацию перед сохранением в админке"""
        obj.clean()
        super().save_model(request, obj, form, change)

admin.site.register(Reservation, ReservationAdmin)
>>>>>>> bddae2e57bd51d9b3a5c0d1ac075d0ae8df1698d
