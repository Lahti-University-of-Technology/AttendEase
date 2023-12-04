from django.db import models
from django.utils.text import slugify
from apps.lecturer.models import Lecture
from apps.users.models import Teacher
from apps.users.models import Student

# Create your models here.
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name="attendace")
    lecture = models.ForeignKey(Lecture, on_delete=models.PROTECT, related_name="attendace")
    marked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.student} - {self.lecture} - {self.marked_at}"
    
    @classmethod
    def entry(cls, student:Student, lecture:Lecture):

        instance = cls.objects.create(student=student, lecture=lecture)
        return instance
