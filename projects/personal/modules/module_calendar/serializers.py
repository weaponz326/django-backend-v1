from rest_framework import serializers
from .models import Calendar, Schedule

class CalendarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calendar
        fields = [
            'id',
            'updated_at',
            'user',
            'calendar_name',
            'created_at',
        ]

class ScheduleSerializer(serializers.ModelSerializer):
    dateStart = serializers.DateTimeField(source='date_start')
    dateEnd = serializers.DateTimeField(source='date_end')
    allDay = serializers.BooleanField(source='all_day')
    backgroundColor = serializers.CharField(source='background_color')

    class Meta:
        model = Schedule
        fields = [
            'id',
            'updated_at',
            'calendar',
            'label',
            'description',
            'dateStart',
            'dateEnd',
            'status',
            'allDay',
            'backgroundColor',
        ]

class ScheduleDaySerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField()
    count = serializers.IntegerField()

    class Meta:
        model = Schedule
        fields = ('created_on', 'count')
