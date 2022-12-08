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

from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=20)
    year = models.IntegerField()
    seats_number = models.IntegerField()
    body_type = models.CharField(max_length=15)
    engine_volume = models.FloatField()
