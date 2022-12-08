from datetime import date

from django.core import validators as v
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

    model = models.CharField(max_length=12)
    year = models.IntegerField(validators=[
        v.MinValueValidator(1950),
        v.MaxValueValidator(date.today().year)
    ], default=2000)
    seats_count = models.IntegerField(default=4)
    body = models.CharField(max_length=12)
    engine_volume = models.FloatField(default=2.0)
    auto_park = models.ForeignKey(AutoParkModel, related_name='cars', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)