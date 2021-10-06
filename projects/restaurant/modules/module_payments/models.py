from django.db import models

from accounts.models import CustomBaseModel, Account
from modules.module_orders.models import Order


# Create your models here.

class Payment(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, to_field='id', on_delete=models.CASCADE, null=True, blank=True)
    payment_code = models.CharField(max_length=50, null=True, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.id)
