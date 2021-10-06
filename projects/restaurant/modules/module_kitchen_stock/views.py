from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import StockItem
from .serializers import StockItemSerializer


# Create your views here.

class StockItemView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        item = StockItem.objects.filter(account=account)
        serializer = StockItemSerializer(item, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StockItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class StockItemDetailView(APIView):
    def get(self, request, id, format=None):
        item = StockItem.objects.get(id=id)
        serializer = StockItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        item = StockItem.objects.get(id=id)
        serializer = StockItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        item = StockItem.objects.get(id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
