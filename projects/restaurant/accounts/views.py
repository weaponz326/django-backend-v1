from django.shortcuts import render
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session

from rest_framework.response import Response
from rest_framework import generics, request, status
from rest_framework import filters
from rest_framework.views import APIView

from .models import Account
from .serializers import AccountSerializer
from modules.module_admin.serializers import UserAccountsSerializer
from modules.module_admin.models import User


# Create your views here.

class AccountView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        profile = Account.objects.filter(account=account)
        serializer = AccountSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        s = SessionStore()
        s['creator_id'] = request.data.get('personal_id')
        s['creator_name'] = request.data.get('personal_name')
        s.save()

        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class AccountDetailView(APIView):
    def get(self, request, id, format=None):
        profile = Account.objects.get(id=id)
        serializer = AccountSerializer(profile)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        profile = Account.objects.get(id=id)
        serializer = AccountSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        profile = Account.objects.get(id=id)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------------------------

# restaurant search

class SearchListView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # TODO:
    # account = request.query_params.get('account', None)
    # exclude_field = [id=account]

class SearchDetailView(APIView):
    def get(self, request, id, format=None):
        search = Account.objects.get(id=id)
        serializer = AccountSerializer(search)
        return Response(serializer.data)

# ----------------------------------------------------------------------------------------------

# checks if user has a restaurant acount
class HasAccountView(APIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(personal_id=request.data.get('personal_id'))
        if user.exists():
            return Response({'has_account': True})
        else:
            return Response({'has_account': False})

# store user selected active account in session
class ActiveAccountView(APIView):
    def post(self, request, *args, **kwargs):
        request.session['active_restaurant'] = True
        request.session['restaurant_id'] = request.data.get('active_account')

        return Response({
            'active_restaurant': request.session['active_restaurant'],
            'restaurant_id': request.session['restaurant_id']
        })

    def get(self, request, *args, **kwargs):
        return Response({
            'active_restaurant': request.session['active_restaurant'],
            'restaurant_id': request.session['restaurant_id']
        })

# get all restaurant suites of a personal id
class UserAccountsView(generics.ListAPIView):
    serializer_class = UserAccountsSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        personal_id = self.request.query_params.get('personal_id', None)
        if personal_id is not None:
            queryset = queryset.filter(personal_id=personal_id)
        return queryset
