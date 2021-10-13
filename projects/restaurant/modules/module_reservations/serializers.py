from rest_framework import serializers

from .models import Reservation
from modules.module_customers.serializers import CustomerSerializer


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = [
            'id',
            'updated_at',
            'account',
            'customer',
            'reservation_code',
            'reservation_date',
            'customer_name',
            'number_guests',
            'number_tables',
            'arrival_date',
            'reservation_status',
        ]

class ReservationDepthSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Reservation
        fields = [
            'id',
            'updated_at',
            'account',
            'customer',
            'reservation_code',
            'reservation_date',
            'customer_name',
            'number_guests',
            'number_tables',
            'arrival_date',
            'reservation_status',
        ]