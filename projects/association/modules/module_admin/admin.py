from django.contrib import admin
from .models import User, Access, Invitation

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'updated_at', 'account', 'personal_id', 'personal_name', 'user_level')

class AccessAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'updated_at', 'admin_access', 'portal_access', 'settings_access')

class InvitationAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'updated_at', 'account', 'invitee_id', 'invitation_status', 'date_sent')

admin.site.register(User, UserAdmin)
admin.site.register(Access, AccessAdmin)
admin.site.register(Invitation, InvitationAdmin)
