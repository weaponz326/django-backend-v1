# Generated by Django 3.2.7 on 2022-01-14 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module_notes', '0002_notefile_file_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NoteFile',
        ),
    ]
