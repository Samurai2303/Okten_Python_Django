from django.urls import path

from .views import ShowAutoParksView, ToggleActiveView, ToggleAdminView, UsersCreateView

urlpatterns = [
    path('', UsersCreateView.as_view()),
    path('/toggle_active/<int:pk>', ToggleActiveView.as_view()),
    path('/toggle_admin/<int:pk>', ToggleAdminView.as_view()),
    path('/auto_parks', ShowAutoParksView.as_view())
]
