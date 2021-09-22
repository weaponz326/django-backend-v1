from django.db import models

from accounts.models import CustomBaseModel,Account


# Create your models here.

class User(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.CASCADE)
    is_creator = models.BooleanField(default=False)
    personal_id = models.CharField(null=True, max_length=200)
    personal_name = models.CharField(null=True, max_length=100)
    user_level = models.CharField(null=True, max_length=20)

    def __str__(self):
        return str(self.id)

class Access(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    id = models.ForeignKey(User, to_field='id', editable=False, on_delete=models.CASCADE)
    admin_access = models.BooleanField(default=False)
    portal_access = models.BooleanField(default=False)
    settings_access = models.BooleanField(default=False)
    stock_access = models.BooleanField(default=False)
    equipment_access = models.BooleanField(default=False)
    purchasing_access = models.BooleanField(default=False)
    orders_access = models.BooleanField(default=False)
    manufacturing_access = models.BooleanField(default=False)
    contractors_access = models.BooleanField(default=False)
    projects_access = models.BooleanField(default=False)
    workers_access = models.BooleanField(default=False)
    tasks_access = models.BooleanField(default=False)
    roster_access = models.BooleanField(default=False)
    materials_access = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class Invitation(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.CASCADE)
    invitee_id = models.CharField(null=True, max_length=200)
    invitee_name = models.CharField(null=True, max_length=200)
    invitation_status = models.CharField(null=True, max_length=30)
    date_sent = models.DateTimeField(null=True, auto_now=True)
    date_confirmed = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.id)
