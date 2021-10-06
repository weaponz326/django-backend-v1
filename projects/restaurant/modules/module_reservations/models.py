from django.db import models

from accounts.models import CustomBaseModel, Account


# Create your models here.

class Reservation(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.CASCADE)
    reservation_code = models.CharField(max_length=50, blank=True)
    reservation_date = models.DateTimeField(null=True, blank=True)
    customer_name = models.CharField(max_length=100, blank=True)
    number_guests = models.IntegerField(blank=True)
    number_tables = models.IntegerField(blank=True)
    arrival_date = models.DateTimeField(null=True, blank=True)
    reservation_status = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.id)
