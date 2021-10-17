from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDay, TruncMonth

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.parsers import FileUploadParser

from .models import Note, NoteFile
from .serializers import NoteSerializer, NoteFileSerializer, NoteAnnotateSerializer


# Create your views here.

class NoteView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        note = Note.objects.filter(user=user)
        serializer = NoteSerializer(note, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NoteDetailView(APIView):
    def get(self, request, id, format=None):
        note = Note.objects.get(id=id)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        note = Note.objects.get(id=id)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        note = Note.objects.get(id=id)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# file attachments

class NoteFileView(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request, format=None):
        note = self.request.query_params.get('note', None)
        file = NoteFile.objects.filter(note=note)
        serializer = NoteFileSerializer(file, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = NoteFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NoteFileDetailView(APIView):
    def get(self, request, id, format=None):
        file = NoteFile.objects.get(id=id)
        serializer = NoteFileSerializer(file)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        file = NoteFile.objects.get(id=id)
        serializer = NoteFileSerializer(file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        file = NoteFile.objects.get(id=id)
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------------------------
# dashboard
# --------------------------------------------------------------------------------------------------------

class CountView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        model = self.request.query_params.get('model', None)
        count = None

        if model == "Note":
            count = Note.objects.filter(user=user).count()

        return Response(count)

class DateAnnotateView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        queryset = Note.objects.filter(user=user).annotate(note_count=Count('created_at'))
        serializer = NoteAnnotateSerializer(queryset)

        # Note.objects
        #     .annotate(month=TruncMonth('created_at'))
        #     .values('month')                      
        #     .annotate(c=Count('id'))              
        #     .values('month', 'c')   

        return Response(serializer.data)