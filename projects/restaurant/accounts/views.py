from django.shortcuts import render
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework import filters
from rest_framework.views import APIView

from .models import Profile
from .serializers import ProfileSerializer


# Create your views here.

class ProfileView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        profile = Profile.objects.filter(account=account)
        serializer = ProfileSerializer(profile, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ProfileDetailView(APIView):
    def get(self, request, pk, format=None):
        profile = Profile.objects.get(id=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile = Profile.objects.get(id=pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        profile = Profile.objects.get(id=pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
