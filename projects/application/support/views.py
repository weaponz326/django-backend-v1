from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import SupportContact
from .serializers import SupportContactSerializer


# Create your views here.

class SupportContactView(APIView):
    def get(self, request, format=None):
        source = self.request.query_params.get('source', None)
        contact = SupportContact.objects.filter(source=source)
        serializer = SupportContactSerializer(contact, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SupportContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class SupportContactDetailView(APIView):
    def get(self, request, pk, format=None):
        account = SupportContact.objects.get(id=pk)
        serializer = SupportContactSerializer(account)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        account = SupportContact.objects.get(id=pk)
        serializer = SupportContactSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        account = SupportContact.objects.get(id=pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
