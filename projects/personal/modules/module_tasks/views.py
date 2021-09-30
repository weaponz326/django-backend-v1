from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Task
from .serializers import TaskSerializer


# Create your views here.

class TaskView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        task = Task.objects.filter(user=user)
        serializer = TaskSerializer(task, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TaskDetailView(APIView):
    def get(self, request, id, format=None):
        task = Task.objects.get(id=id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        task = Task.objects.get(id=id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        task = Task.objects.get(id=id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
