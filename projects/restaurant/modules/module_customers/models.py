from django.db import models

from accounts.models import CustomBaseModel, Account


# Create your models here.

class Customer(CustomBaseModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    customer_code = models.CharField(max_length=50, null=True,  blank=True)
    customer_name = models.CharField(max_length=100, null=True,  blank=True)
    phone = models.CharField(max_length=20, null=True,  blank=True)
    email = models.EmailField(max_length=100, null=True,  blank=True)
    address = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=50, null=True,  blank=True)
    city = models.CharField(max_length=50, null=True,  blank=True)
    post_code = models.CharField(max_length=20, null=True,  blank=True)
    allergies = models.TextField(null=True, blank=True)
    preferences = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
