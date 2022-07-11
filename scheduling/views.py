from django.shortcuts import render
from rest_framework import generics

from scheduling.models import Scheduling
from scheduling.permissions import IsUserOwnerPermission, ListCrateSchedulePermission
from scheduling.serializers import SchedulingReturnSerializer, SchedulingSerializer
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class ListCreateScheduleView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ListCrateSchedulePermission]

    queryset = Scheduling.objects.all()
    serializer_class = SchedulingSerializer

class RetrieveDeleteScheduleView(generics.RetrieveDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsUserOwnerPermission]

    queryset = Scheduling.objects.all()
    serializer_class = SchedulingSerializer

class RetrivieDateScheduleView(generics.ListAPIView):
    serializer_class = SchedulingReturnSerializer

    def get_queryset(self):
        date = self.kwargs['scheduling_date']

        return Scheduling.objects.filter(scheduling_date=date)