from django.urls import path
from . import views

urlpatterns = [
    path("schedule/", views.CreateScheduleView.as_view()),
    path("schedule/all/", views.ListScheduleView.as_view()),
    path("schedule/<int:pk>/", views.RetrieveDeleteScheduleView.as_view()),
    path("schedule/<str:scheduling_date>/", views.RetrivieDateScheduleView.as_view()),
]
