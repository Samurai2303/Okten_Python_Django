from django_filters import rest_framework as filters

from .models import AutoParkModel

# реалізувати фільтрацію автопарків в яких є машини молодше зазначеного року

class AutoParkFilters(filters.FilterSet):
    car_year_gt = filters.NumberFilter('cars', 'year__lt')

    class Meta:
        model = AutoParkModel
        fields = ('car_year_gt',)

    def filter_queryset(self, queryset):
        print(queryset)
        return super().filter_queryset(queryset)

