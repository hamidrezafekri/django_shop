from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


    def archive(self):
        return super().get_queryset()


class BaseModel(models.Model):
    delete_time_stamp = models.DateTimeField(null=True, blank=True, verbose_name=_('delete date'))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('create date'))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_('update date'))
    deleted = models.BooleanField(default=False, verbose_name=_('is deleted'))

    objects = BaseManager()

    def logical_delete(self):
        self.delete_time_stamp = timezone.now()
        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True



class TestModel(BaseModel):
    pass

class MyUserManager(UserManager):

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = 'phone'

    objects = MyUserManager()

    phone = models.CharField(max_length=15, unique=True)
