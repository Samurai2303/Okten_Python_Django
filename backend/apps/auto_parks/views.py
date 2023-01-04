from apps.cars.serializers import CarSerializer
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .filters import AutoParkFilters
from .models import AutoParkModel
from .serializers import AutoParkSerializer


class AutoParksListView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()
    filterset_class = AutoParkFilters
    # permission_classes = (AllowAny,)

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset).distinct()


class AutoParkByIdView(RetrieveUpdateDestroyAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()


class AddCarToAutoParkView(GenericAPIView):
    serializer_class = CarSerializer
    queryset = AutoParkModel.objects.all()

    def get(self, *args, **kwargs):
        auto_park = self.get_object()
        serializer = AutoParkSerializer(auto_park)
        return Response(serializer.data['cars'], status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
