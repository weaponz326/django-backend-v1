from django.db import models
from users.models import CustomBaseModel, User


# Create your models here.

class Budget(CustomBaseModel):
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    budget_name = models.CharField(max_length=100, null=True)
    budget_type = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.id)

class Income(CustomBaseModel):
    budget = models.ForeignKey(Budget, to_field='id', on_delete=models.CASCADE)
    item = models.CharField(max_length=100, null=True)
    amount = models.DecimalField(max_digits=11, decimal_places=2, null=True)

    def __str__(self):
        return str(self.id)

class Expenditure(CustomBaseModel):
    budget = models.ForeignKey(Budget, to_field='id', on_delete=models.CASCADE)
    item = models.CharField(max_length=100, null=True)
    amount = models.DecimalField(max_digits=11, decimal_places=2, null=True)

    def __str__(self):
        return str(self.id)