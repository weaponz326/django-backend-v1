from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.filters import OrderingFilter

from .models import TaskGroup, TaskItem
from .serializers import TaskGroupSerializer, TaskItemSerializer, TaskGroupAnnotateSerializer, TaskItemAnnotateSerializer
from users.paginations import TablePagination


# Create your views here.

class TaskGroupView(APIView, TablePagination):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['task_item', 'priority', 'start_date', 'end_date', 'status']
    ordering = ['-pkid']

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        task_group = TaskGroup.objects.filter(user=user)
        results = self.paginate_queryset(task_group, request, view=self)
        serializer = TaskGroupSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TaskGroupDetailView(APIView):
    def get(self, request, id, format=None):
        task_group = TaskGroup.objects.get(id=id)
        serializer = TaskGroupSerializer(task_group)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        task_group = TaskGroup.objects.get(id=id)
        serializer = TaskGroupSerializer(task_group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        task_group = TaskGroup.objects.get(id=id)
        task_group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------------------------------------
# task item

class AllTaskItemView(APIView, TablePagination):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['task_group', 'created_at']
    ordering = ['-pkid']

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        task_item = TaskItem.objects.filter(task_group__user=user)
        results = self.paginate_queryset(task_item, request, view=self)
        serializer = TaskItemSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

class TaskItemView(APIView):
    def get(self, request, format=None):
        task_group = self.request.query_params.get('task_group', None)
        task_item = TaskItem.objects.filter(task_group=task_group)
        serializer = TaskItemSerializer(task_item, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TaskItemDetailView(APIView):
    def get(self, request, id, format=None):
        task_item = TaskItem.objects.get(id=id)
        serializer = TaskItemSerializer(task_item)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        task_item = TaskItem.objects.get(id=id)
        serializer = TaskItemSerializer(task_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        task_item = TaskItem.objects.get(id=id)
        task_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------------------------
# dashboard
# --------------------------------------------------------------------------------------------------------

class CountView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        model = self.request.query_params.get('model', None)
        count = None

        if model == "Task Group":
            count = TaskGroup.objects.filter(user=user).count()
        elif model == "Task Item":
            count = TaskItem.objects.filter(task_group__user=user).count()

        return Response(count)

class AnnotateView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        model = self.request.query_params.get('model', None)

        if model == "Task Group":
            annotate = TaskGroup.objects.filter(user=user).values(date=TruncDate('created_at')).annotate(count=Count('id')).order_by('date')
            serializer = TaskGroupAnnotateSerializer(annotate, many=True)
            return Response(serializer.data)
        elif model == "Task Item":
            annotate = TaskItem.objects.filter(task_group__user=user).values(date=TruncDate('created_at')).annotate(count=Count('id')).order_by('date')
            serializer = TaskItemAnnotateSerializer(annotate, many=True)
            return Response(serializer.data)
