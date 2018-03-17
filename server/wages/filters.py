import django_filters

from wages import models


class WageFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='istartswith')
    last_name = django_filters.CharFilter(lookup_expr='istartswith')
    government = django_filters.CharFilter(lookup_expr='name__icontains')
    agency = django_filters.CharFilter(lookup_expr='name__icontains')
    dept = django_filters.CharFilter(lookup_expr='name__icontains')
    title = django_filters.CharFilter(lookup_expr='name__icontains')

    order = django_filters.OrderingFilter(
        fields={
            'first_name': 'first_name',
            'last_name': 'last_name',
            'government__name': 'government',
            'agency__name': 'agency',
            'dept__name': 'dept',
            'year': 'year',
        },
    )

    class Meta:
        model = models.Wage
        fields = ['year']
