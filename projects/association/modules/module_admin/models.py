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
    accounts_access = models.BooleanField(default=False)
    members_access = models.BooleanField(default=False)
    committees_access = models.BooleanField(default=False)
    dues_access = models.BooleanField(default=False)
    executives_access = models.BooleanField(default=False)
    action_plan_access = models.BooleanField(default=False)
    budget_access = models.BooleanField(default=False)
    attendance_access = models.BooleanField(default=False)
    meetings_access = models.BooleanField(default=False)
    groups_access = models.BooleanField(default=False)
    year_access = models.BooleanField(default=False)

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
