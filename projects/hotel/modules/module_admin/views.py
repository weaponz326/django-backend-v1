from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status

from .models import User, Access, Invitation
from .serializers import UserSerializer, AccessSerializer, InvitationSerializer
from accounts.models import Account


# Create your views here.

# users

class UserView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        user = User.objects.filter(account=account)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class UserDetailView(APIView):
    def get(self, request, id, format=None):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        user = User.objects.get(id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# access
# ---------------------------------------------------------------------------

class AccessView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        access = Access.objects.filter(account=account)
        serializer = AccessSerializer(access, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.id = request.data.get(id)
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class AccessDetailView(APIView):
    def get(self, request, id, format=None):
        access = Access.objects.get(id=id)
        serializer = AccessSerializer(access)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        access = Access.objects.get(id=id)
        serializer = AccessSerializer(access, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        access = Access.objects.get(id=id)
        access.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -------------------------------------------------------------------------------------------------------

class InvitationView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        invitation = Invitation.objects.filter(account=account)
        serializer = InvitationSerializer(invitation, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InvitationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.id = request.data.get(id)
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class InvitationDetailView(APIView):
    def get(self, request, id, format=None):
        access = Invitation.objects.get(id=id)
        serializer = InvitationSerializer(access)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        access = Invitation.objects.get(id=id)
        serializer = InvitationSerializer(access, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        access = Invitation.objects.get(id=id)
        access.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------------------------------------------
# signals

@receiver(post_save, sender=Account)
def save_user(sender, instance, created, **kwargs):
    if created:
        s = SessionStore()

        User.objects.create(
            account=Account.objects.get(id=instance.id),
            is_creator=True,
            # personal_id=s['creator_id'],
            # personal_name=s['creator_name'],
            user_level="Admin",
        )

@receiver(post_save, sender=User)
def save_access(sender, instance, created, **kwargs):
    if created:
        if instance.user_level == "Admin":
            Access.objects.create(
                id=User.objects.get(id=instance.id),
                admin_access=True,
                portal_access=True,
                settings_access=True,
                bills_access=True,
                staff_access=True,
                guests_access=True,
                roster_access=True,
                payments_access=True,
                services_access=True,
                checkin_access=True,
                bookings_access=True,
                rooms_access=True,
                assets_access=True,
                housekeeping_access=True,
            )
        else:
            Access.objects.create(id=User.objects.get(id=instance.id))

