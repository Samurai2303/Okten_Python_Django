from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from apps.auto_parks.models import AutoParkModel
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer

from .serializers import AutoParkSerializer


class AutoParksListCreateAPIView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()


class AutoParkByIdView(RetrieveUpdateDestroyAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        qs = CarModel.objects.filter(auto_park=pk)
        serializer = CarSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        auto_park = self.get_object()

        data: dict = self.request.data
        data['auto_park'] = auto_park.pk

        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        auto_park_serializer = AutoParkSerializer(auto_park)
        return Response(auto_park_serializer.data, status=status.HTTP_201_CREATED)
