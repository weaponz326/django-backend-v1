from datetime import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
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
    all_objects = CustomBaseManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

class User(AbstractUser, CustomBaseModel):
    location = models.CharField(max_length=255)
    about = models.TextField()
    photo = models.FileField(null=True, blank=True, upload_to='user_profile')

    REQUIRED_FIELDS = ['first_name', 'last_name', 'location', 'about']

    def __str__(self):
        return str(self.id)
