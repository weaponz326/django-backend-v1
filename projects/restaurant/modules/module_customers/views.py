from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Customer
from .serializers import CustomerSerializer, CustomerSerializer


# Create your views here.

class CustomerView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        customer = Customer.objects.filter(account=account)
        serializer = CustomerSerializer(customer, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CustomerDetailView(APIView):
    def get(self, request, id, format=None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        customer = Customer.objects.get(id=id)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------------------------
# dashboard
# --------------------------------------------------------------------------------------------------------

class CountView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        model = self.request.query_params.get('model', None)
        count = None

        if model == "Customer":
            count = Customer.objects.filter(account=account).count()

        return Response(count)
