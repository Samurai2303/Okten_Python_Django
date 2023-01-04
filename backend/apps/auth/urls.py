from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ActivateUserView, RecoverySendEmailView, RecoverySetPasswordView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view()),
    path('/activate/<str:token>', ActivateUserView.as_view()),
    path('/recovery/<str:email>', RecoverySendEmailView.as_view()),
    path('/recovery/<str:token>/<str:password>', RecoverySetPasswordView.as_view())
]
