from rest_framework import serializers

from .models import Rink
from users.serializers import UserSerializer


class RinkSerializer(serializers.ModelSerializer):

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

class RinkDepthSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    recipient = UserSerializer()

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

class RinkAnnotateSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    count = serializers.IntegerField()

    class Meta:
        model = Rink
        fields = [
            'created_at',
            'date',
            'count'
        ]
