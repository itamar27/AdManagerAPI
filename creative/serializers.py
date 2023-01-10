from rest_framework import serializers

from . import models


class CreativeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Creative
        fields = '__all__'
