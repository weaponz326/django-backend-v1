from django.contrib import admin

from .models import User


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'first_name', 'last_name', 'email')

admin.site.register(User, UserAdmin)
