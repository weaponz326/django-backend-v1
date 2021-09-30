from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status

from .models import Appointment
from .serializers import AppointmentSerializer


# Create your views here.

class AppointmentView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        appointment = Appointment.objects.filter(user=user)
        serializer = AppointmentSerializer(appointment, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.id = request.data.get(id)
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class AppointmentDetailView(APIView):
    def get(self, request, id, format=None):
        access = Appointment.objects.get(id=id)
        serializer = AppointmentSerializer(access)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        access = Appointment.objects.get(id=id)
        serializer = AppointmentSerializer(access, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        access = Appointment.objects.get(id=id)
        access.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
