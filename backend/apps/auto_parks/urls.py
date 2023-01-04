from django.urls import path

from .views import AddCarToAutoParkView, AutoParkByIdView, AutoParksListView

urlpatterns = [
    path('', AutoParksListView.as_view(), name='auto_parks_list_create'),
    path('/<int:pk>', AutoParkByIdView.as_view()),
    path('/<int:pk>/cars', AddCarToAutoParkView.as_view())
]
