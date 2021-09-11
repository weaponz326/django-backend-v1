from datetime import timezone
from django.db import models
from django.db.models.query import QuerySet


class BaseUtilityManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(BaseUtilityManager, self).__init__(*args, *kwargs)

        def get_queryset(self):
            if self.alive_only:
                return BaseUtilityManager(self.model).filter(deleted_at=None)
            return BaseUtilityQuerySet(self.model)

class BaseUtilityQuerySet(QuerySet):
    def delete(self):
        return super(BaseUtilityQuerySet, self).update(deleted_at=timezone.now())
    
    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)