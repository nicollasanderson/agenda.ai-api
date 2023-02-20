from django.urls import path
from . import views

urlpatterns = [
    path("user/", views.CreateUserView.as_view()),
    path("user/all/", views.ListUsersView.as_view()),
    path("user/login/", views.MyTokenObtainPairView.as_view()),
    path("user/<pk>/", views.ListUpdateDeleteUserView.as_view()),
]
