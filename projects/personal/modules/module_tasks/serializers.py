from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'updated_at',
            'user',
            'task_name',
            'description',
            'task_time',
            'status',
        ]
