from typing import Type

from django.contrib.auth import get_user_model

from apps.users.models import UserModel as User
from core.enums.action_enum import ActionEnum
from core.exceptions.jwt_exception import JWTException
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.tokens import BlacklistMixin, Token

UserModel: Type[User] = get_user_model()

TokenClass = Type[BlacklistMixin | Token]


class ActivateToken(BlacklistMixin, Token):
    lifetime = ActionEnum.ACTIVATE.lifetime
    token_type = ActionEnum.ACTIVATE.token_type


class RecoveryToken(BlacklistMixin, Token):
    lifetime = ActionEnum.RECOVERY.lifetime
    token_type = ActionEnum.RECOVERY.token_type


class JWTService:

    @staticmethod
    def create_token(user, token_class: TokenClass):
        return token_class.for_user(user)

    @staticmethod
    def validate_token(token, token_class: TokenClass):
        try:
            token_res = token_class(token)
            token_res.check_blacklist()
        except (Exception,):
            raise JWTException
        token_res.blacklist()
        user_id = token_res.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)
