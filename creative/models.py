import uuid

from django.db import models


class Creative(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=256)
    content = models.TextField()
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    line_items = models.ForeignKey("line_item.LineItem", on_delete=models.CASCADE, related_name='creatives')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
