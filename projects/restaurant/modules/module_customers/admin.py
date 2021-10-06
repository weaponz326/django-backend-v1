from django.contrib import admin

from .models import Customer


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'customer_code', 'customer_name', 'phone')

admin.site.register(Customer, CustomerAdmin)
