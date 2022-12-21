from django.db import models

from apps.users.models import UserModel


class AutoParkModel(models.Model):
    class Meta:
        db_table = 'auto_parks'
        ordering = ['id']

    name = models.CharField(max_length=15)
    users = models.ManyToManyField(UserModel, through='UsersAutoParksModel', related_name='auto_parks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UsersAutoParksModel(models.Model):
    class Meta:
        db_table = 'users_auto_parks'

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE)
