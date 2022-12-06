from django.urls import path
from . import views

urlpatterns = [
    path("room/", views.CreateRoomView.as_view()),
    path("rooms/", views.ListRoomsView.as_view()),
    path("room/<pk>", views.ListOneRoomView.as_view()),
    path("room/<blockName>/", views.ListBlockRoomView.as_view()),
]
