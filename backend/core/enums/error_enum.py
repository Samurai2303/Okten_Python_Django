from enum import Enum

from rest_framework import status


class ErrorEnum(Enum):
    JWT: ({'details': 'token invalid or expired'}, status.HTTP_200_OK)

    def __init__(self, msg: dict, status_code):
        self.msg = msg
        self.status_code = status_code
