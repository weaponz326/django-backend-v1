from django.contrib import admin

from .models import Account


# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'name', 'location')

admin.site.register(Account, AccountAdmin)
