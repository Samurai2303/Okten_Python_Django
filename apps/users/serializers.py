from typing import Type

from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework.serializers import ModelSerializer

from apps.auto_parks.serializers import AutoParkSerializer
from apps.users.models import UserModel as User

from .models import ProfileModel, UserPhotosModel

UserModel: Type[User] = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('name', 'surname', 'age', 'phone')


class UserSerializer(ModelSerializer):
    auto_parks = AutoParkSerializer(many=True, read_only=True)
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at',
            'auto_parks', 'profile', 'last_login')
        read_only_fields = ('id', 'is_active', 'is_superuser', 'is_staff', 'created_at', 'updated_at', 'last_login')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @transaction.atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        return user


class UserPhotosSerializer(ModelSerializer):
    class Meta:
        model = UserPhotosModel
        fields = ('photos',)
