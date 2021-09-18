from django.shortcuts import render
from django.db.models.functions import TruncDay
from django.db.models import Count

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins, status, filters
from rest_framework.permissions import IsAuthenticated

from .models import Rink
from .serializers import RinkSerializer


# Create your views here.


class RinkView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        rink = Rink.objects.filter(user=user)
        serializer = RinkSerializer(rink, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RinkSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class RinkDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        rink = Rink.objects.get(id=id)
        serializer = RinkSerializer(rink)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        rink = Rink.objects.get(id=id)
        serializer = RinkSerializer(rink, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        rink = Rink.objects.get(id=id)
        rink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# list all incoming and outgoing rinks of a user
class RinkListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RinkSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rink_date']
    ordering = ['-rink_date']

    def get_queryset(self):
        queryset = Rink.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(sender__id=user) | queryset.filter(recipient__id=user)
        return queryset

# -----------------------------------------------------------------------------------------------------
# dashboard

class CountRinkDateListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RinkSerializer

    def get_queryset(self):
        queryset = Rink.objects.all()
        # counts = queryset.annotate(date=TruncDay('rink_date')).values("date").annotate(count=Count('id'))
        # return counts
