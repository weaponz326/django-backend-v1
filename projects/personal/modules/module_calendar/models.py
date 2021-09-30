from django.db import models
from users.models import CustomBaseModel, User

# Create your models here.


class Appointment(CustomBaseModel):
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    label = models.CharField(null=True, blank=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    date_start = models.DateTimeField(null=True, blank=True)
    date_end = models.DateTimeField(null=True, blank=True)
    status = models.CharField(null=True, blank=True, max_length=20)
    all_day = models.BooleanField(default=False)
    background_color = models.CharField(null=True, blank=True, max_length=20)

    def __str__(self):
        return str(self.id)
