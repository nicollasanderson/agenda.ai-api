from django.shortcuts import render
from rest_framework import generics

from rooms.models import Room
from rooms.permissions import GetRoomPermission
from rooms.serializers import RoomSerializer

from rest_framework.authentication import TokenAuthentication

from users.permissions import IsSuperUserPermission

# Create your views here.


class CreateRoomView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserPermission]

    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ListRoomsView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [GetRoomPermission]

    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ListOneRoomView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [GetRoomPermission]

    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ListBlockRoomView(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        block = self.kwargs["blockName"]
        return Room.objects.filter(block=block)
