import django_filters
from .models import *

class ProductFilter(django_filters.FilterSet):
    keyword = django_filters.filters.CharFilter(field_name='name',lookup_expr='icontains')
    minprice = django_filters.filters.NumberFilter(field_name='price' or 0,lookup_expr='gte')
    maxprice = django_filters.filters.NumberFilter(field_name='price' or 10000,lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['minprice', 'maxprice', 'keyword']