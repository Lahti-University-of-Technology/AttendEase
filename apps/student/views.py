from django.shortcuts import render
from apps.lecturer.views import Lecture
from django.views.generic import ListView 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required(login_url="login"), name="dispatch")
class LectureInfoView(ListView):
    model = Lecture
    template_name = 'dashboard/student/lecture_info.html'


    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.user.is_student:
            return queryset.filter(course__course_enroll__student__user=self.request.user)

        return queryset


