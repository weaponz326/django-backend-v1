from django.shortcuts import render
from django.db.models import Count

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionDepthSerializer, TransactionSerializer


# Create your views here.

class AccountView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        account = Account.objects.filter(user=user)
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class AccountDetailView(APIView):
    def get(self, request, id, format=None):
        account = Account.objects.get(id=id)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        account = Account.objects.get(id=id)
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        account = Account.objects.get(id=id)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------------------------------------------------------------------------
# transactions

class TransactionView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        transaction = Transaction.objects.filter(account=account)
        serializer = TransactionSerializer(transaction, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TransactionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TransactionDetailView(APIView):
    def get(self, request, id, format=None):
        transaction = Transaction.objects.get(id=id)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        transaction = Transaction.objects.get(id=id)
        serializer = TransactionSerializer(transaction, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        transaction = Transaction.objects.get(id=id)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# all transactions
class AllTransactionsView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        account = Transaction.objects.filter(account__user=user)
        serializer = TransactionDepthSerializer(account, many=True)
        return Response(serializer.data)

# --------------------------------------------------------------------------------------------------------
# dashboard
# --------------------------------------------------------------------------------------------------------

class CountView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        model = self.request.query_params.get('model', None)
        count = None

        if model == "Account":
            count = Account.objects.filter(user=user).count()
        elif model == "Transaction":
            count = Transaction.objects.filter(account__user=user).count()

        return Response(count)
