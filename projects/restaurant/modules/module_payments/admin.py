from django.contrib import admin
from .models import Payment


# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'order', 'payment_code', 'amount_paid')

admin.site.register(Payment, PaymentAdmin)
