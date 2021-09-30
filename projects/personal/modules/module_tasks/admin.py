from django.contrib import admin
from .models import Task


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'updated_at', 'user', 'task_name', 'status')

admin.site.register(Task, TaskAdmin)
