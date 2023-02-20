from django.urls import path
from . import views

urlpatterns = [
    path("schedule/", views.CreateScheduleView.as_view()),
    path("schedule/all/", views.ListScheduleView.as_view()),
    path("schedule/<pk>/", views.RetrieveDeleteScheduleView.as_view()),
    path(
        "schedule/<str:scheduling_date>/date/", views.RetrivieDateScheduleView.as_view()
    ),
    path("schedule/<str:user_id>/user/", views.RetrivieByUserScheduleView.as_view()),
]
