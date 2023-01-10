from rest_framework import viewsets
from . import models
from . import serializers


class AdUnitViewset(viewsets.ModelViewSet):

    queryset = models.AdUnit.objects.all()
    serializer_class = serializers.AdUnitSerializer