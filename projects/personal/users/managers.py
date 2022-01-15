from django.utils import timezone
from django.db import models
from django.db.models.query import QuerySet


class CustomBaseManager(models.Manager):
    # def __init__(self, *args, **kwargs):
    #     self.alive_only = kwargs.pop('alive_only', True)
    #     super(CustomBaseManager, self).__init__(*args, *kwargs)

    #     def get_queryset(self):
    #         if self.alive_only:
    #             return CustomBaseManager(self.model).filter(deleted_at=None)
    #         return CustomBaseQuerySet(self.model)
            
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)
    

class CustomBaseQuerySet(QuerySet):
    def delete(self):
        return super(CustomBaseQuerySet, self).update(deleted_at=timezone.now())

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)
