# Generated by Django 3.2.7 on 2022-01-07 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_accounts', '0002_auto_20210927_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
