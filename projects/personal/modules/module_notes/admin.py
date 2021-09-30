from django.contrib import admin
from .models import Note, NoteFile

# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'updated_at', 'user', 'subject', 'created_at')

class NoteFileAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'updated_at', 'note', 'file')

admin.site.register(Note, NoteAdmin)
admin.site.register(NoteFile, NoteFileAdmin)
