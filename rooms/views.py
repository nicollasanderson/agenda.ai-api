from django.shortcuts import render
from rest_framework import generics

from rooms.models import Room
from rooms.serializers import RoomSerializer

from rest_framework.authentication import TokenAuthentication

from users.permissions import IsSuperUserPermission

# Create your views here.

class ListCreateRoom(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserPermission]

    queryset = Room.objects.all()
    serializer_class = RoomSerializer