from django.db import models
from django.db.models.fields import BigAutoField
import uuid

# Create your models here.

class SupportContact(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()
    source = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)