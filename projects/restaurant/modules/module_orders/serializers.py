from rest_framework import serializers

from .models import Order, OrderItem
from modules.module_customers.serializers import CustomerSerializer


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = [
            'id',
            'updated_at',
            'account',
            'customer',
            'order_code',
            'order_date',
            'customer_name',
            'order_type',
            'order_status',
            'order_total',
        ]

class OrderDepthSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = [
            'id',
            'updated_at',
            'account',
            'customer',
            'order_code',
            'order_date',
            'customer_name',
            'order_type',
            'order_status',
            'order_total',
        ]

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = [
            'id',
            'updated_at',
            'order',
            'menu_item',
            'quantity',
        ]
