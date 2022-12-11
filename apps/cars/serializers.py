from rest_framework.serializers import ModelSerializer

from .models import CarModel, CarPhotosModel


class CarPhotoSerializer(ModelSerializer):
    class Meta:
        model = CarPhotosModel
        fields = ('photo',)


class CarSerializer(ModelSerializer):
    photos = CarPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = CarModel
        exclude = ('auto_park',)
