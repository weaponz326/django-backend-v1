from rest_framework import serializers

from .models import Payment
from modules.module_orders.serializers import OrderSerializer


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = [
            'id',
            'updated_at',
            'account',
            'order',
            'payment_code',
            'payment_date',
            'amount_paid',
        ]

class PaymentDepthSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = Payment
        fields = [
            'id',
            'updated_at',
            'account',
            'order',
            'payment_code',
            'payment_date',
            'amount_paid',
        ]
