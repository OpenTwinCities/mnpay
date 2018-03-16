from rest_framework import viewsets
from wages import models
from wages import serializers


class WageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing Wage information
    """
    queryset = models.Wage.objects.all()
    serializer_class = serializers.WageSerializer
