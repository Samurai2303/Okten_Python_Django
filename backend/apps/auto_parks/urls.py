from django.urls import path

from .views import AddCarToAutoParkView, AutoParkByIdView, AutoParksListView

urlpatterns = [
    path('', AutoParksListView.as_view()),
    path('/<int:pk>', AutoParkByIdView.as_view()),
    path('/<int:pk>/cars', AddCarToAutoParkView.as_view())
]
