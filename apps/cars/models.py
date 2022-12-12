from django.db import models

from apps.auto_parks.models import AutoParkModel

from .services import upload_car_photo


class CarModel(models.Model):

    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=15, unique=True)
    body = models.CharField(max_length=12)
    year = models.IntegerField()
    seats_count = models.IntegerField()
    engine_volume = models.FloatField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CarPhotosModel(models.Model):
    class Meta:
        db_table = 'car_photos'
        
    photos = models.ImageField(upload_to=upload_car_photo, blank=True)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='car_photos')
