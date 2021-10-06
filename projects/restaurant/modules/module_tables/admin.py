from django.contrib import admin

from .models import Table


# Register your models here.

class TableAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'table_number', 'table_type', 'table_status')

admin.site.register(Table, TableAdmin)
