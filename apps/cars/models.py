from django.db import models

from apps.auto_parks.models import AutoParkModel

# Створити модель CarModel з такими полями:
# - марка машини
# - рік випуску
# - кількість місць
# - тип кузову
# - об'єм двигуна (float)
#
# реалізувати всі CRUD операції
#
# ***при виведені всіх машин показувати тільки (id, марку машини та рік)

class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=15, unique=True)
    year = models.IntegerField()
    seats_count = models.IntegerField()
    body = models.CharField(max_length=12)
    engine_volume = models.FloatField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
