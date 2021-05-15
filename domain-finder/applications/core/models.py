from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True


class TimeStampBaseModel(BaseModel):
    created_at = models.DateTimeField(auto_created=True)
    update_at = models.DateTimeField(auto_created=True)

    class Meta:
        abstract = True
