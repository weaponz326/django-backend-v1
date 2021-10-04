from rest_framework import serializers
from .models import TaskGroup, TaskItem


class TaskGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskGroup
        fields = [
            'id',
            'updated_at',
            'user',
            'task_group',
            'created_at',
        ]

class TaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = [
            'id',
            'updated_at',
            'task_group',
            'task_item',
            'description',
            'task_time',
            'status',
        ]
