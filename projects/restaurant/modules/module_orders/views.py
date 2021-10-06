from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer


# Create your views here.

class OrderView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        order = Order.objects.filter(account=account)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class OrderDetailView(APIView):
    def get(self, request, id, format=None):
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        order = Order.objects.get(id=id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderTotalView(APIView):
    def patch(self, request, id, format=None):
        total = Order.objects.get(id=id)
        serializer = OrderSerializer(total, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# ----------------------------------------------------------------------------------------------------------
# order item

class OrderItemView(APIView):
    def get(self, request, format=None):
        order = self.request.query_params.get('order', None)
        item = OrderItem.objects.filter(order=order)
        serializer = OrderItemSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class OrderItemDetailView(APIView):
    def get(self, request, id, format=None):
        item = OrderItem.objects.get(id=id)
        serializer = OrderItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        item = OrderItem.objects.get(id=id)
        serializer = OrderItemSerializer(item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        item = OrderItem.objects.get(id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
