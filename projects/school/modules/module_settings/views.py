from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins, status

from .models import ExtendedProfile, Subscription
from accounts.models import Account
from .serializers import ExtendedProfileSerializer, SubscriptionSerializer


# Create your views here.


class ExtendedProfileView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        profile = ExtendedProfile.objects.filter(id=account)
        serializer = ExtendedProfileSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExtendedProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ExtendedProfileDetailView(APIView):
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

# ---------------------------------------------------------------------------------------------------
# subscriptions

class SubscriptionView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        subscription = Subscription.objects.filter(account=account)
        serializer = SubscriptionSerializer(subscription, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class SubscriptionDetailView(APIView):
    def get(self, request, id, format=None):
        subscription = Subscription.objects.get(id=id)
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        subscription = Subscription.objects.get(id=id)
        serializer = SubscriptionSerializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        subscription = Subscription.objects.get(id=id)
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------------------------------------------

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        ExtendedProfile.objects.create(
            id=Account.objects.get(id=instance.id)
        )

        Subscription.objects.create(
            id=Account.objects.get(id=instance.id),
            subscription_type="Individual"
        )
