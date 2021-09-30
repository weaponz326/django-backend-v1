from django.db import models
from users.models import CustomBaseModel, User


# Create your models here.

class Account(CustomBaseModel):
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100, null=True)
    account_number = models.CharField(max_length=50, null=True)
    bank_name = models.CharField(max_length=100, null=True)
    account_type = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.id)

class Transaction(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(null=True)
    description = models.CharField(max_length=100, null=True)
    transaction_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=11, decimal_places=2, null=True)

    def __str__(self):
        return str(self.id)
