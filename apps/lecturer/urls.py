from django.urls import path
# from attendease import views
from .views import CreateLectureView

urlpatterns = [
    path("dashboard/new_lecture", CreateLectureView.as_view(), name="CreateLectureView"),
]