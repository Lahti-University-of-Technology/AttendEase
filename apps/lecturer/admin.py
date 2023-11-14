from django.contrib import admin
from .models import Lecture, Course, CourseEnrollment

# Register your models here.
admin.site.register(Lecture)
admin.site.register(Course)
admin.site.register(CourseEnrollment)