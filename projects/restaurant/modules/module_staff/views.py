from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Staff
from .serializers import StaffSerializer, StaffListSerializer


# Create your views here.

class StaffView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        staff = Staff.objects.filter(account=account)
        serializer = StaffListSerializer(staff, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class StaffDetailView(APIView):
    def get(self, request, id, format=None):
        staff = Staff.objects.get(id=id)
        serializer = StaffSerializer(staff)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        staff = Staff.objects.get(id=id)
        serializer = StaffSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        staff = Staff.objects.get(id=id)
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------------------------
# dashboard
# --------------------------------------------------------------------------------------------------------

class CountView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        model = self.request.query_params.get('model', None)
        count = None

        if model == "Staff":
            count = Staff.objects.filter(account=account).count()

        return Response(count)
