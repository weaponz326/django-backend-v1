# Generated by Django 3.2.7 on 2022-01-24 11:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('module_calendar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('label', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_start', models.DateTimeField(blank=True, null=True)),
                ('date_end', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('all_day', models.BooleanField(default=False)),
                ('background_color', models.CharField(blank=True, max_length=20, null=True)),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_calendar.calendar', to_field='id')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
