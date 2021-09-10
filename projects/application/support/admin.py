from django.contrib import admin

from .models import SupportContact


# Register your models here.

class SupportContactAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'name', 'email')

admin.site.register(SupportContact, SupportContactAdmin)
