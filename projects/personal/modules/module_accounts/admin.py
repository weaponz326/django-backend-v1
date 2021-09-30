from django.contrib import admin
from .models import Account, Transaction


# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'user', 'account_name', 'bank_name')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'transaction_date', 'transaction_type', 'amount')

admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
