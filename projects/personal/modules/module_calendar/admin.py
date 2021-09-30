from django.contrib import admin
from .models import Appointment

# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'updated_at', 'user', 'label', 'date_start', 'date_end', 'status')

admin.site.register(Appointment, AppointmentAdmin)
