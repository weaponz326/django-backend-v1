from django.contrib import admin

from .models import Reservation


# Register your models here.

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'reservation_code', 'reservation_date', 'reservation_status')

admin.site.register(Reservation, ReservationAdmin)
