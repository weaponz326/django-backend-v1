# Generated by Django 3.2.7 on 2021-10-05 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module_orders', '0001_initial'),
        ('module_payments', '0002_alter_payment_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='module_orders.order', to_field='id'),
        ),
    ]
