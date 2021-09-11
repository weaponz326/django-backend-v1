from datetime import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from .managers import BaseUtilityManager


# Create your models here.

class BaseUtilityModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = BaseUtilityManager()
    all_objects = BaseUtilityManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

class Profile(BaseUtilityModel):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    logo = models.FileField(null=True, blank=True, upload_to='account_profile')

    def __str__(self):
        return str(self.name)
