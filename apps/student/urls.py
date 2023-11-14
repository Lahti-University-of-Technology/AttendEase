from django.urls import path
from .views import LectureInfoView

urlpatterns = [
    path("dashboard/lecture_info/", LectureInfoView.as_view(), name="lecture-info"),
]