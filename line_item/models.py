import uuid

from django.db import models
from django.core.validators import MinValueValidator


class LineItem(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    max_impressions = models.PositiveIntegerField()
    rpm = models.FloatField(
        validators=[MinValueValidator(0)]
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    targeting = models.ManyToManyField("ad_unit.AdUnit", related_name='line_items', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
