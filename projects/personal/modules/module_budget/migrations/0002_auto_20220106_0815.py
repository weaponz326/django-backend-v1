# Generated by Django 3.2.7 on 2022-01-06 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_budget', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenditure',
            old_name='item',
            new_name='item_description',
        ),
        migrations.RenameField(
            model_name='income',
            old_name='item',
            new_name='item_description',
        ),
        migrations.AddField(
            model_name='expenditure',
            name='item_number',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='income',
            name='item_number',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
