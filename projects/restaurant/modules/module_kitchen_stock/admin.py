from django.contrib import admin

from .models import StockItem


# Register your models here.

class StockItemAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'item_code', 'item_name', 'quantity')

admin.site.register(StockItem, StockItemAdmin)
