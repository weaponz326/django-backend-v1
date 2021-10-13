# Generated by Django 3.2.7 on 2021-10-08 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module_customers', '0002_alter_customer_account'),
        ('module_reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='module_customers.customer', to_field='id'),
        ),
    ]
