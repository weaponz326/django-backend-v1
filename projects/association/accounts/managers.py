from datetime import timezone
from django.db import models
from django.db.models.query import QuerySet


def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)
        
class CustomBaseQuerySet(QuerySet):
    def delete(self):
        return super(CustomBaseQuerySet, self).update(deleted_at=timezone.now())
    
    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)