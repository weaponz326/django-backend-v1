from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id',
            'created_at',
            'updated_at',
            'name',
            'location',
            'about',
            'logo',
        ]
