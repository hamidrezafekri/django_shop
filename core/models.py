from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract=True
class TimeStampMixin(BaseModel):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

