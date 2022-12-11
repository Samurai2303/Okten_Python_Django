from django.db import models


class CarManager(models.Manager):
    def lt_year(self, year: int):
        return self.filter(year__lt=year)
