# Generated by Django 3.2.7 on 2021-10-06 08:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_rename_profile_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sitting',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('sitting_code', models.CharField(blank=True, max_length=20, null=True)),
                ('sitting_date', models.DateField(blank=True, null=True)),
                ('arrival_time', models.TimeField(blank=True, null=True)),
                ('departure_time', models.TimeField(blank=True, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('number_guests', models.IntegerField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account', to_field='id')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]