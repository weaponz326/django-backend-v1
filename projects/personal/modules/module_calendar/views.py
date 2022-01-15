from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter

from .models import Calendar, Schedule
from .serializers import CalendarSerializer, ScheduleSerializer, ScheduleAnnotateSerializer
from users.paginations import TablePagination

# Create your views here.
class CalendarView(APIView, TablePagination):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['calendar_name', 'created_at']
    ordering = ['-pkid']

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        calendar = Calendar.objects.filter(user=user)
        results = self.paginate_queryset(calendar, request, view=self)
        serializer = CalendarSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

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

class ScheduleView(APIView, TablePagination):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['schedule_name', 'start_date', 'end_date', 'status']
    ordering = ['-pkid']

    def get(self, request, format=None):
        calendar = self.request.query_params.get('calendar', None)
        schedule = Schedule.objects.filter(calendar=calendar)
        results = self.paginate_queryset(schedule, request, view=self)
        serializer = ScheduleSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

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

class AnnotateView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        model = self.request.query_params.get('model', None)

        if model == "Schedule":
            annotate = Schedule.objects.filter(calendar__user=user).values(date=TruncDate('created_at')).annotate(count=Count('id')).order_by('date')
            serializer = ScheduleAnnotateSerializer(annotate, many=True)
            return Response(serializer.data)
