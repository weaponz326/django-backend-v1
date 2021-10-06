from django.contrib import admin

from .models import Order, OrderItem


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'order_code', 'order_date', 'order_status')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'order', 'menu_item', 'quantity')

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
