from django.shortcuts import render
from django.db.models import Count

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status

from .models import Calendar, Schedule
from .serializers import CalendarSerializer, ScheduleSerializer


# Create your views here.

class CalendarView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        calendar = Calendar.objects.filter(user=user)
        serializer = CalendarSerializer(calendar, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CalendarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.id = request.data.get(id)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CalendarDetailView(APIView):
    def get(self, request, id, format=None):
        access = Calendar.objects.get(id=id)
        serializer = CalendarSerializer(access)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        access = Calendar.objects.get(id=id)
        serializer = CalendarSerializer(access, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        access = Calendar.objects.get(id=id)
        access.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -------------------------------------------------------------------------------------
# schedule

class ScheduleView(APIView):
    def get(self, request, format=None):
        calendar = self.request.query_params.get('calendar', None)
        schedule = Schedule.objects.filter(calendar=calendar)
        serializer = ScheduleSerializer(schedule, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.id = request.data.get(id)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ScheduleDetailView(APIView):
    def get(self, request, id, format=None):
        access = Schedule.objects.get(id=id)
        serializer = ScheduleSerializer(access)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        access = Schedule.objects.get(id=id)
        serializer = ScheduleSerializer(access, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        access = Schedule.objects.get(id=id)
        access.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------------------------
# dashboard
# --------------------------------------------------------------------------------------------------------

class CountView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        model = self.request.query_params.get('model', None)
        count = None

        if model == "Calendar":
            count = Calendar.objects.filter(user=user).count()
        elif model == "Schedule":
            count = Schedule.objects.filter(calendar__user=user).count()

        return Response(count)

class ScheduleDayAnnotateView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        annotation = Schedule.objects.filter(calendar__user=user).annotate(schedule_count=Count('created_at'))
        return Response(annotation)
