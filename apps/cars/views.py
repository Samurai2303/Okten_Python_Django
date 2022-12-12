from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import CarModel, CarPhotosModel
from .serializers import CarPhotosSerializer, CarSerializer


class CarsListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

class CarByIdView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

class AddPhotosToCarView(GenericAPIView):
    serializer_class = CarPhotosSerializer
    queryset = CarModel.objects.all()

    def patch(self, *args, **kwargs):
        car = self.get_object()
        files = self.request.FILES
        for key in files:
            serializer = self.serializer_class(data={'photos':files[key]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        car = self.get_object()
        serializer = CarSerializer(car)
        return Response(serializer.data.car_photos, status=status.HTTP_200_OK)