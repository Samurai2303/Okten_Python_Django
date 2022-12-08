from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarsListAPIView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        query_params = self.request.query_params.dict()
        auto_park_id = query_params.get('auto_park_id')
        if auto_park_id:
            print(auto_park_id)
            queryset = queryset.filter(auto_park=auto_park_id)
        return queryset


class CarRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
