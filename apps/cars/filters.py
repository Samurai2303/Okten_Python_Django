from django_filters import rest_framework as filters

from .models import CarModel


class CarFilters(filters.FilterSet):
    price_gt = filters.NumberFilter('price', 'gt')
    price_gte = filters.NumberFilter('price', 'gte')
    price_lt = filters.NumberFilter('price', 'lt')
    model_start = filters.CharFilter('model', 'istartswith')
    model_end = filters.CharFilter('model', 'iendswith')
    model_contain = filters.CharFilter('model', 'icontains')

    class Meta:
        model = CarModel
        fields = ('price_gt', 'price_gte', 'price_lt', 'model_start', 'model_end', 'model_contain')
