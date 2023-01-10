from rest_framework import serializers

from creative.serializers import CreativeSerializer
from . import models


class LineItemSerializer(serializers.ModelSerializer):

    creatives = CreativeSerializer(many=True, read_only=True)

    class Meta:
        model = models.LineItem
        fields = '__all__'
