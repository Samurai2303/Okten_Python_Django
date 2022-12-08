from django.urls import path

from .views import AutoParkByIdView, AutoParksListCreateView

urlpatterns = [
    path('', AutoParksListCreateView.as_view()),
    path('/<int:pk>', AutoParkByIdView.as_view())
]
