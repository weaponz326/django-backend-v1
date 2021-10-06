from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Sitting
from .serializers import SittingSerializer


# Create your views here.

class SittingView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        sitting = Sitting.objects.filter(account=account)
        serializer = SittingSerializer(sitting, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SittingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class SittingDetailView(APIView):
    def get(self, request, id, format=None):
        sitting = Sitting.objects.get(id=id)
        serializer = SittingSerializer(sitting)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        sitting = Sitting.objects.get(id=id)
        serializer = SittingSerializer(sitting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        sitting = Sitting.objects.get(id=id)
        sitting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
