from django.contrib import admin
from .models import TaskGroup, TaskItem


# Register your models here.

class TaskGroupAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'updated_at', 'user', 'task_group', 'created_at')

class TaskItemAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'updated_at', 'task_group', 'task_item', 'status')

admin.site.register(TaskGroup, TaskGroupAdmin)
admin.site.register(TaskItem, TaskItemAdmin)
