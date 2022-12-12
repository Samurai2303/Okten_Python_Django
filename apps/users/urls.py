from django.urls import path

from .views import AddAutoParkView, AddPhotosToProfileView, ToggleActiveView, ToggleAdminView, UsersListCreateView

urlpatterns = [
    path('', UsersListCreateView.as_view()),
    path('/<int:pk>/toggle_active', ToggleActiveView.as_view()),
    path('/<int:pk>/toggle_admin', ToggleAdminView.as_view()),
    path('/add_auto_park', AddAutoParkView.as_view()),
    path('/add_photos', AddPhotosToProfileView.as_view())
]
