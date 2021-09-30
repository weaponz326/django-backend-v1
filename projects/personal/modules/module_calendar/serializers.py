from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    dateStart = serializers.DateTimeField(source='date_start')
    dateEnd = serializers.DateTimeField(source='date_end')
    allDay = serializers.BooleanField(source='all_day')
    backgroundColor = serializers.CharField(source='background_color')

    class Meta:
        model = Appointment
        fields = [
            'id',
            'updated_at',
            'user',
            'label',
            'description',
            'dateStart',
            'dateEnd',
            'status',
            'allDay',
            'backgroundColor',
        ]