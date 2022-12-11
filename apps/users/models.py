from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as val
from django.db import models

from .enums import RegEx
from .managers import UserManager
from .services import upload_avatar


class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, validators=[
        val.RegexValidator(RegEx.PASSWORD.pattern, RegEx.PASSWORD.message)
    ])
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profiles'

    name = models.CharField(max_length=18, validators=[
        val.RegexValidator(RegEx.NAME.pattern, RegEx.NAME.message)
    ])
    surname = models.CharField(max_length=20, validators=[
        val.RegexValidator(RegEx.NAME.pattern, RegEx.NAME.message)
    ])
    age = models.IntegerField(validators=[
        val.MinValueValidator(1), val.MaxValueValidator(100)
    ])
    house = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, validators=[
        val.RegexValidator(RegEx.PHONE.pattern, RegEx.PHONE.message)
    ])
    avatar = models.ImageField(upload_to=upload_avatar, blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
