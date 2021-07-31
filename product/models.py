from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from core.models import TimeStampMixin, BaseModel


class Discount(TimeStampMixin):
    pass

class Price(TimeStampMixin):
    pass

class DiscountCode(TimeStampMixin):
    pass


class Category(TimeStampMixin):
    pass


class Status(TimeStampMixin):
    pass


class Product(TimeStampMixin):
    name = models.CharField(verbose_name=_('name'),help_text=_('enter product name'),
                            max_length=200,blank=False,null=False)
    Image = models.FileField(_('image'),upload_to='Product')
