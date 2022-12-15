from rest_framework import status
from rest_framework.response import Response
from core.services.jwt_service import JWTService, ActivateToken, RecoveryToken
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.generics import get_object_or_404
from typing import Type
from django.contrib.auth import get_user_model
from apps.users.models import UserModel as User
from core.services.email_service import EmailService
from .serializers import PasswordSerializer

UserModel: Type[User] = get_user_model()


class ActivateUserView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        token = kwargs.get('token')
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)


class RecoverySendEmailView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        email = kwargs.get('email')
        user = get_object_or_404(UserModel, email=email)
        EmailService.recovery_password(user)
        return Response(status=status.HTTP_200_OK)


class RecoverySetPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        token = kwargs.get('token')
        new_password = kwargs.get('password')
        serializer = PasswordSerializer(data=new_password)
        serializer.is_valid(raise_exception=True)
        user = JWTService.validate_token(token, RecoveryToken)
        user.set_password(new_password)
        user.save()
        return Response({'details': 'password saved'}, status=status.HTTP_200_OK)
