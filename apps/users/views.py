from typing import Type

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.auto_parks.serializers import AutoParkSerializer
from apps.users.models import UserModel as User

from .permissions import IsSuperUser
from .serializers import UserSerializer

UserModel: Type[User] = get_user_model()


class ShowAutoParksView(GenericAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def get_object(self) -> User:
        return self.request.user

    def get(self, *args, **kwargs):
        auto_parks = self.get_object().auto_parks
        serializer = AutoParkSerializer(auto_parks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        user = self.get_object()
        data = self.request.data
        serializer = AutoParkSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UsersCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)


class ToggleActiveView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return self.queryset.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
        else:
            user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ToggleAdminView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)

    def get_queryset(self):
        return self.queryset.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            user.is_staff = False
        else:
            user.is_staff = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
