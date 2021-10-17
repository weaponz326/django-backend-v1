
from rest_framework import serializers
from .models import Note, NoteFile

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

class NoteFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoteFile
        fields = [
            'id',
            'updated_at',
            'note',
            'file',
        ]
        
class NoteAnnotateSerializer(serializers.ModelSerializer):
    note_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Note
        fields = [
            'id',
            'created_at',
            'note_count',
        ]