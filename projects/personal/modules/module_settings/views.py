from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated

from .models import ExtendedProfile
from users.models import User
from .serializers import ExtendedProfileSerializer


# Create your views here.


class ExtendedProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        profile = ExtendedProfile.objects.filter(user=user)
        serializer = ExtendedProfileSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExtendedProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ExtendedProfileDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        rink = ExtendedProfile.objects.get(id=id)
        serializer = ExtendedProfileSerializer(rink)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        rink = ExtendedProfile.objects.get(id=id)
        serializer = ExtendedProfileSerializer(rink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        rink = ExtendedProfile.objects.get(id=id)
        rink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------------------------------------------

@receiver(post_save, sender=User)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        ExtendedProfile.objects.create(id=instance.id)
