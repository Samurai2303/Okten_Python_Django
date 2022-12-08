from django.urls import path

from .views import AutoParkByIdView, AutoParksListCreateAPIView

urlpatterns = [
    path('', AutoParksListCreateAPIView.as_view()),
    path('/<int:pk>', AutoParkByIdView.as_view())
]
