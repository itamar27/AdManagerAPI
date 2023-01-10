from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from . import (
    models, serializers, utils
)


class LineItemsViewset(viewsets.ModelViewSet):

    queryset = models.LineItem.objects.all()
    serializer_class = serializers.LineItemSerializer

    @action(detail=False, methods=['GET'], url_path='filter')
    def get_line_items_filtered(self, request):
        try:
            filters = utils.create_ad_unit_filter_dict(self.request.query_params.dict())
        except KeyError:
            return Response("Not a valid query parameter", status.HTTP_400_BAD_REQUEST)

        filtered_qs = self.queryset.filter(**filters)
        response = self.get_serializer(filtered_qs, many=True)

        return Response(response.data)


