from django.db import models
from django.utils import timezone


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):
    delete_time_stamp = models.DateTimeField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = BaseManager()

    def logical_delete(self):
        self.delete_time_stamp = timezone.now()
        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True
