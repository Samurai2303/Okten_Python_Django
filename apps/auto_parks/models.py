from django.db import models

from apps.users.models import UserModel


class AutoParkModel(models.Model):
    class Meta:
        db_table = 'auto_parks'

    name = models.CharField(max_length=15)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auto_parks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
