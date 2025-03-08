from django.contrib import admin
from .models import Customer

<<<<<<< HEAD
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name', 'phone')
=======
admin.site.register(Customer)
>>>>>>> bddae2e57bd51d9b3a5c0d1ac075d0ae8df1698d
