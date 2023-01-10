from rest_framework import serializers

from line_item.serializers import LineItemSerializer
from . import models


class AdUnitSerializer(serializers.ModelSerializer):

    line_items = LineItemSerializer(many=True, read_only=True)

    class Meta:
        model = models.AdUnit
        fields = '__all__'
        extra_kwargs = {'line_items': {'required': False}}
