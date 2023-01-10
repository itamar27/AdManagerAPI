from rest_framework import viewsets
from . import models
from . import serializers


class CreativeViewset(viewsets.ModelViewSet):

    queryset = models.Creative.objects.all()
    serializer_class = serializers.CreativeSerializer
