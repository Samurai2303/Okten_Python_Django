from django.urls import path

from .views import AddPhotosToCarView, CarByIdView, CarsListView

urlpatterns = [
    path('', CarsListView.as_view()),
    path('/<int:pk>', CarByIdView.as_view()),
    path('/<int:pk>/photos', AddPhotosToCarView.as_view())
]
