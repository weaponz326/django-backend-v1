# Generated by Django 3.2.7 on 2021-10-18 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_profile_account'),
        ('module_settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subscription_type', models.CharField(blank=True, max_length=30, null=True)),
                ('billing_frequency', models.CharField(blank=True, max_length=30, null=True)),
                ('number_users', models.IntegerField(blank=True, null=True)),
                ('id', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='accounts.account', to_field='id')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
