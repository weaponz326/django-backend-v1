# Generated by Django 3.2.7 on 2021-09-26 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('budget_name', models.CharField(max_length=100, null=True)),
                ('budget_type', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='id')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('item', models.CharField(max_length=100, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11, null=True)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_budget.budget', to_field='id')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('item', models.CharField(max_length=100, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11, null=True)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_budget.budget', to_field='id')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]