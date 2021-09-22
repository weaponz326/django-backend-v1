from django.contrib import admin

from .models import ExtendedProfile


# Register your models here.

class ExtendedProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'updated_at', 'email', 'phone', 'country')

admin.site.register(ExtendedProfile, ExtendedProfileAdmin)
