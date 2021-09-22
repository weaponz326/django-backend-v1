from rest_framework import serializers

from .models import Rink
from accounts.serializers import AccountSerializer


class RinkSerializer(serializers.ModelSerializer):
    sender = None
    recipient = None

    class Meta:
        model = Rink
        fields = [
            'id',
            'created_at',
            'updated_at',
            'sender',
            'recipient',
            'rink_date',
            'rink_type',
            'rink_source',
            'comment',
        ]

    def __init__(self, *args, **kwargs):
        super(RinkSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            pass
        else:
            self.sender = AccountSerializer()
            self.recipient = AccountSerializer()
