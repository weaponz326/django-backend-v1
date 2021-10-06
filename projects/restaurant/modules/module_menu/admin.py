from django.contrib import admin

from .models import MenuGroup, MenuItem


# Register your models here.

class MenuGroupAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'menu_group', 'category')

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'menu_group', 'item_code', 'item_name', 'price')

admin.site.register(MenuGroup, MenuGroupAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
