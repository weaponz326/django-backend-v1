from django.db import models

from accounts.models import CustomBaseModel, Account
from modules.module_orders.models import Order


# Create your models here.

class Delivery(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, to_field='id', on_delete=models.CASCADE, null=True, blank=True)
    delivery_code = models.CharField(max_length=50, null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    customer_name = models.CharField(max_length=200, null=True, blank=True)
    customer_location = models.CharField(max_length=200, null=True, blank=True)
    delivery_status = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.id)