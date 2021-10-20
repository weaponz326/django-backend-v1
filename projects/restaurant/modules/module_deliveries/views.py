from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Delivery
from .serializers import DeliverySerializer


# Create your views here.

class DeliveryView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        delivery = Delivery.objects.filter(account=account)
        serializer = DeliverySerializer(delivery, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DeliverySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeliveryDetailView(APIView):
    def get(self, request, id, format=None):
        delivery = Delivery.objects.get(id=id)
        serializer = DeliverySerializer(delivery)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        delivery = Delivery.objects.get(id=id)
        serializer = DeliverySerializer(delivery, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        delivery = Delivery.objects.get(id=id)
        delivery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------------------------
# dashboard
# --------------------------------------------------------------------------------------------------------

class CountView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        model = self.request.query_params.get('model', None)
        count = None

        if model == "Delivery":
            count = Delivery.objects.filter(account=account).count()

        return Response(count)
