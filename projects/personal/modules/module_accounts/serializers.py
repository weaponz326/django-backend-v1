from rest_framework import serializers
from .models import Account, Transaction


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id',
            'updated_at',
            'user',
            'account_name',
            'account_number',
            'bank_name',
            'account_type',
        ]

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'id',
            'updated_at',
            'account',
            'transaction_date',
            'description',
            'amount',
            'transaction_type',
        ]

class TransactionDepthSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = Transaction
        fields = [
            'id',
            'updated_at',
            'account',
            'transaction_date',
            'description',
            'amount',
            'transaction_type',
        ]
