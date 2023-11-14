from django.urls import path
# from attendease import views
from .views import CreateLectureView, LectureListView

urlpatterns = [
    path("new_lecture/", CreateLectureView.as_view(), name="create-lecture"),
    path("lecture_list/", LectureListView.as_view(), name="lecture-list"),
]