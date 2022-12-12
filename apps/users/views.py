from typing import Type

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializers import AutoParkSerializer
from apps.users.models import UserModel as User

from .models import UserPhotosModel
from .permissions import IsSupereuser
from .serializers import ProfileSerializer, UserPhotosSerializer, UserSerializer

UserModel: Type[User] = get_user_model()


class UsersListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAdminUser,)


class ToggleActiveView(GenericAPIView):
    serializer_class = UserSerializer
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
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsSupereuser,)

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


class AddAutoParkView(GenericAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()

    def get(self, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data.auto_parks, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        user = self.request.user
        data = self.request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AddPhotosToProfileView(GenericAPIView):
    serializer_class = UserPhotosSerializer
    queryset = UserPhotosModel.objects.all()

    def patch(self, *args, **kwargs):
        profile = self.request.user.profile
        files = self.request.FILES
        for key in files:
            serializer = self.serializer_class(data={'photos': files[key]})
            serializer.is_valid(raise_exception=True)
            serializer.save(profile=profile)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
