from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Table
from .serializers import TableSerializer


# Create your views here.

class TableView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        table = Table.objects.filter(account=account)
        serializer = TableSerializer(table, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TableDetailView(APIView):
    def get(self, request, id, format=None):
        table = Table.objects.get(id=id)
        serializer = TableSerializer(table)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        table = Table.objects.get(id=id)
        serializer = TableSerializer(table, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        table = Table.objects.get(id=id)
        table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------------------------
# dashboard
# --------------------------------------------------------------------------------------------------------

class CountView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        model = self.request.query_params.get('model', None)
        count = None

        if model == "Table":
            count = Table.objects.filter(account=account).count()

        return Response(count)
