from django.urls import path

from .views import CarByIdView, CarsView

urlpatterns = [
    path('', CarsView.as_view()),
    path('/<int:pk>', CarByIdView.as_view())
]
