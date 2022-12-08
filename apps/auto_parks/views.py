from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.cars.serializers import CarSerializer

from .models import AutoParkModel
from .serializers import AutoParkSerializer


class AutoParksListCreateView(ListAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return AllowAny(),
        return IsAuthenticated(),


class AutoParkByIdView(RetrieveUpdateDestroyAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()

    def post(self, *args, **kwargs):
        auto_park = self.get_object()

        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)

        serializer = AutoParkSerializer(auto_park)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
