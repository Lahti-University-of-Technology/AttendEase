from django.http import HttpResponse
from django.shortcuts import render

from apps.lecturer.models import Lecture

# Create your views here.
def index(request):
    return render(request, "attendease/homepage.html")

def dashboard(request):
    return render(request, "dashboard/base.html")


from django.shortcuts import render
from django.views.generic import CreateView as GCV
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from .models import Attendance
# Create your views here.


class CreateAttendaceView(GCV):
    """
    TODO: implement logic to mark attendance.
     - get user from request
     - validate that the requested user is student or not
     - save it
    """
    model = Lecture
    queryset = Lecture.objects.all()

    def post(self, request, *args, **kwargs):
        self.object = None
        lecture = self.get_object()
        user = request.user

        if not user.is_student:
            return HttpResponse("Only Student Can Mark There Attendance")
        
        attendace = Attendance.entry(user, lecture)
        
        return HttpResponse(f"Successfully marked attanced for {attendace.lecture.title}.")

