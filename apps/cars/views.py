from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import CarModel
from .serializers import CarPhotoSerializer, CarSerializer


class CarsListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()


class CarByIdView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class LtYearListCarsView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        year = self.request.query_params.get('year')
        if year:
            return CarModel.objects.lt_year(year)
        return self.queryset


class AddCarPhotoView(GenericAPIView):
    serializer_class = CarPhotoSerializer
    queryset = CarModel

    def post(self, *args, **kwargs):
        car = self.get_object()
        files = self.request.FILES
        for key in files:
            serializer = self.serializer_class(data={'photo': files[key]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
