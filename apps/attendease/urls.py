from django.urls import path
# from attendease import views
from .views import CreateAttendaceView, AttendanceDetailView

urlpatterns = [
    # path("dashboard/", dashboard, name="dashboard"),
    path("mark/<str:slug>/", CreateAttendaceView.as_view(), name="mark-attendance"),
    path("detail/", AttendanceDetailView.as_view(), name="attendance-detail"),
    path("attendance-info/<str:pk>/", AttendanceDetailView.as_view(), name="attendance-inffo"),
]