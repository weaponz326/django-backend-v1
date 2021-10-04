from django.db import models
from users.models import CustomBaseModel, User


# Create your models here.

class TaskGroup(CustomBaseModel):
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    task_group = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.id)

class TaskItem(CustomBaseModel):
    task_group = models.ForeignKey(TaskGroup, to_field='id', on_delete=models.CASCADE)
    task_item = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True, blank=True)
    task_date = models.DateField(null=True)
    status = models.BooleanField(null=True)

    def __str__(self):
        return str(self.id)
