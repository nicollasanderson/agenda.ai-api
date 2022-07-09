from django.urls import path
from . import views

urlpatterns = [
    path('room/', views.ListCreateRoom.as_view()),
]