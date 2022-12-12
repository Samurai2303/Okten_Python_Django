from rest_framework.serializers import ModelSerializer

from .models import CarModel, CarPhotosModel


class CarPhotosSerializer(ModelSerializer):
    class Meta:
        model = CarPhotosModel
        fields = ('photos',)


class CarSerializer(ModelSerializer):
    car_photos = CarPhotosSerializer(many=True, read_only=True)

    class Meta:
        model = CarModel
        exclude = ('auto_park',)
