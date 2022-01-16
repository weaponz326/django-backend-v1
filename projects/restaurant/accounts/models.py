from datetime import timezone
from django.db import models
import uuid

from .managers import CustomBaseManager


# Create your models here.

class CustomBaseModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = CustomBaseManager()

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

class Account(CustomBaseModel):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    logo = models.FileField(null=True, blank=True, upload_to='account_profile')

    def __str__(self):
        return str(self.id)
