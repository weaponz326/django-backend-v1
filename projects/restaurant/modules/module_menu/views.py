from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import MenuGroup, MenuItem
from .serializers import MenuGroupSerializer, MenuItemSerializer


# Create your views here.

class MenuGroupView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        menu_group = MenuGroup.objects.filter(account=account)
        serializer = MenuGroupSerializer(menu_group, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MenuGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class MenuGroupDetailView(APIView):
    def get(self, request, id, format=None):
        menu_group = MenuGroup.objects.get(id=id)
        serializer = MenuGroupSerializer(menu_group)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        menu_group = MenuGroup.objects.get(id=id)
        serializer = MenuGroupSerializer(menu_group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        menu_group = MenuGroup.objects.get(id=id)
        menu_group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------------------------------------
# menu items

class MenuItemView(APIView):
    def get(self, request, format=None):
        menu_group = self.request.query_params.get('menu_group', None)
        item = MenuItem.objects.filter(menu_group=menu_group)
        serializer = MenuItemSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class MenuItemDetailView(APIView):
    def get(self, request, id, format=None):
        item = MenuItem.objects.get(id=id)
        serializer = MenuItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        item = MenuItem.objects.get(id=id)
        serializer = MenuItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        item = MenuItem.objects.get(id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------------------------
# dashboard
# --------------------------------------------------------------------------------------------------------

class CountView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        model = self.request.query_params.get('model', None)
        count = None

        if model == "Menu Group":
            count = MenuGroup.objects.filter(account=account).count()
        elif model == "Menu Item":
            count = MenuItem.objects.filter(menu_group__account=account).count()

        return Response(count)
