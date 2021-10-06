from django.contrib import admin

from .models import Sitting


# Register your models here.

class SittingAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'sitting_code', 'sitting_date', 'customer_name')

admin.site.register(Sitting, SittingAdmin)
