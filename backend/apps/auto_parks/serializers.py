from apps.cars.serializers import CarSerializer
from rest_framework.serializers import ModelSerializer

from .models import AutoParkModel


class AutoParkSerializer(ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'cars', 'users', 'created_at', 'updated_at')
        depth = 1
