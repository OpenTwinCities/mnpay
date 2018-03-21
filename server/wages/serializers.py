from rest_framework import serializers
from wages import models


class WageSerializer(serializers.ModelSerializer):
    title = serializers.StringRelatedField()
    dept = serializers.StringRelatedField()
    agency = serializers.StringRelatedField()
    government = serializers.StringRelatedField()


    class Meta:
        model = models.Wage
        fields = (
            'title', 'dept', 'agency', 'government', 'first_name', 'last_name',
            'middle_name', 'wage', 'year'
        )
