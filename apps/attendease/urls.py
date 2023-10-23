from django.urls import path
# from attendease import views
from .views import CreateAttendaceView, index, dashboard

urlpatterns = [
    path("", index, name="index"),
    path("dashboard/", dashboard, name="dashboard"),
    path("mark/<str:slug>/", CreateAttendaceView.as_view(), name="mark-attendance"),
]