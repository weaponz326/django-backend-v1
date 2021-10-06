from django.contrib import admin
from .models import Roster, Shift, Batch, StaffPersonnel, RosterDay, RosterSheet


# Register your models here.

class RosterAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'roster_code', 'roster_name')

class ShiftAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'roster', 'shift_name', 'start_time', 'end_time')

class BatchAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'roster', 'batch_name', 'batch_symbol')

class StaffPersonnelAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'roster', 'staff', 'batch')

class RosterDayAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'roster', 'day')

class RosterSheetAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'roster_day', 'shift', 'batch')

admin.site.register(Roster, RosterAdmin)
admin.site.register(Shift, ShiftAdmin)
admin.site.register(Batch, BatchAdmin)
admin.site.register(StaffPersonnel, StaffPersonnelAdmin)
admin.site.register(RosterDay, RosterDayAdmin)
admin.site.register(RosterSheet, RosterSheetAdmin)
