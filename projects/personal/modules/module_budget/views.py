from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Budget, Income, Expenditure
from .serializers import BudgetSerializer, IncomeSerializer, ExpenditureSerializer, IncomeAnnotateSerializer, ExpenditureAnnotateSerializer


# Create your views here.

class BudgetView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        budget = Budget.objects.filter(user=user)
        serializer = BudgetSerializer(budget, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class BudgetDetailView(APIView):
    def get(self, request, id, format=None):
        budget = Budget.objects.get(id=id)
        serializer = BudgetSerializer(budget)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        budget = Budget.objects.get(id=id)
        serializer = BudgetSerializer(budget, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        budget = Budget.objects.get(id=id)
        budget.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# income
# --------------------------------------------------------------------------------------------------

class IncomeView(APIView):
    def get(self, request, format=None):
        budget = self.request.query_params.get('budget', None)
        income = Income.objects.filter(budget=budget)
        serializer = IncomeSerializer(income, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class IncomeDetailView(APIView):
    def get(self, request, id, format=None):
        income = Income.objects.get(id=id)
        serializer = IncomeSerializer(income)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        income = Income.objects.get(id=id)
        serializer = IncomeSerializer(income, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        income = Income.objects.get(id=id)
        income.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# income
# --------------------------------------------------------------------------------------------------

class ExpenditureView(APIView):
    def get(self, request, format=None):
        budget = self.request.query_params.get('budget', None)
        expenditure = Expenditure.objects.filter(budget=budget)
        serializer = ExpenditureSerializer(expenditure, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExpenditureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ExpenditureDetailView(APIView):
    def get(self, request, id, format=None):
        expenditure = Expenditure.objects.get(id=id)
        serializer = ExpenditureSerializer(expenditure)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        expenditure = Expenditure.objects.get(id=id)
        serializer = ExpenditureSerializer(expenditure, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        expenditure = Expenditure.objects.get(id=id)
        expenditure.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------------------------
# dashboard
# --------------------------------------------------------------------------------------------------------

class CountView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        model = self.request.query_params.get('model', None)
        count = None

        if model == "Budget":
            count = Budget.objects.filter(user=user).count()
        elif model == "Income":
            count = Income.objects.filter(budget__user=user).count()
        elif model == "Expenditure":
            count = Expenditure.objects.filter(budget__user=user).count()

        return Response(count)

class AnnotateView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        model = self.request.query_params.get('model', None)

        if model == "Income":
            annotate = Income.objects.filter(budget__user=user).values(date=TruncDate('created_at')).annotate(count=Count('id')).order_by('date')
            serializer = IncomeAnnotateSerializer(annotate, many=True)
            return Response(serializer.data)
        elif model == "Expenditure":
            annotate = Expenditure.objects.filter(budget__user=user).values(date=TruncDate('created_at')).annotate(count=Count('id')).order_by('date')
            serializer = ExpenditureAnnotateSerializer(annotate, many=True)
            return Response(serializer.data)
