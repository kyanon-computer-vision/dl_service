# from django.db import models
from djongo import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-last_modified']
