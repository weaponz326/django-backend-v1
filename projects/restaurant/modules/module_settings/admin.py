from django.contrib import admin

from .models import ExtendedProfile, Subscription


# Register your models here.

class ExtendedProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'updated_at', 'email', 'phone', 'country')

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'updated_at', 'subscription_type', 'billing_frequency', 'number_users')

admin.site.register(ExtendedProfile, ExtendedProfileAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
