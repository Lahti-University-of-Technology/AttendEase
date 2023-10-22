from django.db import models
from .constants import COURSES, CLASSROOMS

# Create your models here.
class Lecture(models.Model):
    title = models.CharField(max_length=100)
    start_date =models.DateTimeField()
    start_time = models.DateTimeField()
    end_date = models.DateTimeField()
    end_time = models.DateTimeField()
    lecture_created = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    course = models.CharField(choices=COURSES, max_length=100)
    classroom = models.CharField(choices=CLASSROOMS, max_length=100)

    def __str__(self):
        return self.title