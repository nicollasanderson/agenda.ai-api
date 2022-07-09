from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.CreateUserView.as_view()),
    path('user/all/', views.ListUsersView.as_view()),
    path('user/login/', views.LoginView.as_view()),
    path('user/<int:pk>/', views.ListUpdateDeleteUserView.as_view()),
]