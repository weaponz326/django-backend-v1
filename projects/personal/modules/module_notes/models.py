from django.db import models
from users.models import CustomBaseModel, User

# Create your models here.


class Note(CustomBaseModel):
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    subject = models.CharField(null=True, blank=True, max_length=200)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
