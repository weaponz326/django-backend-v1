from django.contrib import admin

from .models import Delivery


# Register your models here.

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'delivery_code', 'order', 'delivery_status')

admin.site.register(Delivery, DeliveryAdmin)
