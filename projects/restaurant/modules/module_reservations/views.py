from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Reservation
from .serializers import ReservationSerializer, ReservationDepthSerializer


# Create your views here.

class ReservationView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        reservation = Reservation.objects.filter(account=account)
        serializer = ReservationDepthSerializer(reservation, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ReservationDetailView(APIView):
    def get(self, request, id, format=None):
        reservation = Reservation.objects.get(id=id)
        serializer = ReservationDepthSerializer(reservation)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        reservation = Reservation.objects.get(id=id)
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        reservation = Reservation.objects.get(id=id)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------------------------
# dashboard
# --------------------------------------------------------------------------------------------------------

class CountView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        model = self.request.query_params.get('model', None)
        count = None

        if model == "Reservation":
            count = Reservation.objects.filter(account=account).count()

        return Response(count)
