from django.urls import path
from . import views

urlpatterns = [
    path('schedule/', views.ListCreateScheduleView.as_view()),
    path('schedule/<int:pk>', views.RetrieveDeleteScheduleView.as_view()),
]