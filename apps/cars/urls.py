from django.urls import path

from.views import CarByIdView, CarsListView
urlpatterns = [
    path('', CarsListView.as_view()),
    path('/<int:pk>', CarByIdView.as_view())
]