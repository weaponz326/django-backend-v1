from django.db import models
import uuid

from accounts.models import CustomBaseModel, Account


# Create your models here.

class ExtendedProfile(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    id = models.ForeignKey(Account, to_field='id', editable=False, on_delete=models.CASCADE)
    country = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

class Subscription(CustomBaseModel):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    id = models.ForeignKey(Account, to_field='id', editable=False, on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length=30, null=True, blank=True)
    billing_frequency = models.CharField(max_length=30, null=True, blank=True)
    number_users = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
