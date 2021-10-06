from rest_framework import serializers

from .models import Delivery


class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = [
            'id',
            'updated_at',
            'account',
            'order',
            'delivery_code',
            'delivery_date',
            'customer_name',
            'customer_location',
            'delivery_status',
        ]

    def __init__(self, *args, **kwargs):
        super(DeliverySerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1