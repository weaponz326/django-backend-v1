from django.db import models

from accounts.models import CustomBaseModel, Account


# Create your models here.

class StockItem(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.CASCADE)
    item_code = models.CharField(max_length=20, null=True, blank=True)
    item_name = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    item_type = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    refill_ordered = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
