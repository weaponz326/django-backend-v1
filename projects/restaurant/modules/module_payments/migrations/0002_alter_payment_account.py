# Generated by Django 3.2.7 on 2021-10-04 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_profile_account'),
        ('module_payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account', to_field='id'),
        ),
    ]
