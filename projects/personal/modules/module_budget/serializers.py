from rest_framework import serializers
from .models import Budget, Income, Expenditure

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = [
            'id',
            'updated_at',
            'user',
            'budget_name',
            'budget_type',
            'created_at',
        ]

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = [
            'id',
            'updated_at',
            'budget',
            'item',
            'amount',
        ]
        
class ExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenditure
        fields = [
            'id',
            'updated_at',
            'budget',
            'item',
            'amount',
        ]

class IncomeAnnotateSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    count = serializers.IntegerField()

    class Meta:
        model = Income
        fields = [
            'created_at',
            'date',
            'count'
        ]

class ExpenditureAnnotateSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    count = serializers.IntegerField()

    class Meta:
        model = Expenditure
        fields = [
            'created_at',
            'date',
            'count'
        ]
