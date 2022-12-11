from django.urls import path

from .views import AddAvatarView, ShowAutoParksView, ToggleActiveView, ToggleAdminView, UsersListCreateView

urlpatterns = [
    path('', UsersListCreateView.as_view()),
    path('/toggle_active/<int:pk>', ToggleActiveView.as_view()),
    path('/toggle_admin/<int:pk>', ToggleAdminView.as_view()),
    path('/auto_parks', ShowAutoParksView.as_view()),
    path('/avatar', AddAvatarView.as_view())
]

