from django.db import models

from accounts.models import CustomBaseModel, Account
from modules.module_menu.models import MenuItem


# Create your models here.

class Order(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.CASCADE)
    order_code = models.CharField(max_length=50, blank=True)
    order_date = models.DateTimeField(null=True, blank=True)
    customer_name = models.CharField(max_length=100, null=True, blank=True)
    order_type = models.CharField(max_length=50, null=True, blank=True)
    order_status = models.CharField(max_length=50, null=True, blank=True)
    order_total = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return str(self.id)

class OrderItem(CustomBaseModel):
    order = models.ForeignKey(Order, to_field='id', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
