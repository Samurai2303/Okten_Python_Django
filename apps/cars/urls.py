from django.urls import path

from .views import AddCarPhotoView, CarByIdView, CarsListView, LtYearListCarsView

urlpatterns = [
    path('', CarsListView.as_view()),
    path('/<int:pk>', CarByIdView.as_view()),
    path('/lt_year', LtYearListCarsView.as_view()),
    path('/<int:pk>/photos', AddCarPhotoView.as_view())
]
