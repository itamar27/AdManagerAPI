import uuid

from django.db import models


class AdUnit(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=256)
    language = models.CharField(max_length=256)
    device = models.CharField(max_length=256)
    os = models.CharField(max_length=10)
    browser = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['country', 'language', 'device', 'os', 'browser']
