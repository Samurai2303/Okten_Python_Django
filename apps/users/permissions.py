from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsSupereuser(BasePermission):
    def has_permission(self, request: Request, view):
        return bool(request.user.is_staff and request.user and request.user.is_active and request.user.is_superuser)
