from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import CarModel
from .serializers import CarSerializer


class CarsListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

class CarByIdView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
