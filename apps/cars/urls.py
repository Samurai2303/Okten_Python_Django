from django.urls import path

from .views import CarRetrieveUpdateDestroyAPIView, CarsListAPIView

urlpatterns = [
    path('', CarsListAPIView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroyAPIView.as_view())
]
