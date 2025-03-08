from django.contrib import admin
from .models import Table

<<<<<<< HEAD
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'seats', 'is_available')
    list_filter = ('is_available',)
=======
admin.site.register(Table)
>>>>>>> bddae2e57bd51d9b3a5c0d1ac075d0ae8df1698d
