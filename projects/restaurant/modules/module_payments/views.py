from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Payment
from .serializers import PaymentSerializer, PaymentDepthSerializer


# Create your views here.

class PaymentView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        payment = Payment.objects.filter(account=account)
        serializer = PaymentDepthSerializer(payment, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PaymentDetailView(APIView):
    def get(self, request, id, format=None):
        payment = Payment.objects.get(id=id)
        serializer = PaymentDepthSerializer(payment)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        payment = Payment.objects.get(id=id)
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        payment = Payment.objects.get(id=id)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------------------------
# dashboard
# --------------------------------------------------------------------------------------------------------

class CountView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        model = self.request.query_params.get('model', None)
        count = None

        if model == "Payment":
            count = Payment.objects.filter(account=account).count()

        return Response(count)
