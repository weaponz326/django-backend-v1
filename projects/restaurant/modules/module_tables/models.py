from django.db import models

from accounts.models import CustomBaseModel, Account


# Create your models here.

class Table(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.CASCADE)
    table_number = models.CharField(max_length=20, null=True, blank=True)
    table_type = models.CharField(max_length=50, null=True, blank=True)
    capacity = models.CharField(max_length=9, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    table_status = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.id)
