
from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = [
            'id',
            'updated_at',
            'created_at',
            'user',
            'subject',
            'body',
        ]

class NoteAnnotateSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    count = serializers.IntegerField()

    class Meta:
        model = Note
        fields = [
            'created_at',
            'date',
            'count'
        ]
