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
    parents_access = models.BooleanField(default=False)
    assessment_access = models.BooleanField(default=False)
    subjects_access = models.BooleanField(default=False)
    attendance_access = models.BooleanField(default=False)
    students_access = models.BooleanField(default=False)
    reports_access = models.BooleanField(default=False)
    teachers_access = models.BooleanField(default=False)
    staff_access = models.BooleanField(default=False)
    payments_access = models.BooleanField(default=False)
    classes_access = models.BooleanField(default=False)
    timetable_access = models.BooleanField(default=False)
    fees_access = models.BooleanField(default=False)
    sections_access = models.BooleanField(default=False)

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
