from django.urls import path,include
from api import api_v1

urlpatterns = [
    path('api/v1', include('api.api_v1'))
]