from io import BytesIO
from django.conf import settings
from urllib.parse import urljoin
import qrcode
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from apps.users.models import Teacher, Student
from config.helpers import image_path
from .constants import COURSES, CLASSROOMS
from django.core.files.base import ContentFile


# Create your models here.
class Course(models.Model): 
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=120)
    created_by = models.ForeignKey(Teacher, on_delete=models.PROTECT, related_name="lecture_creater", null=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs) -> None:
      
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)


class CourseEnrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name="stu_course_enroll",  null=True, blank=True)
    Course = models.ManyToManyField(Course, related_name="course_enroll")

    def __str__(self):
        return self.student.user.username
    

class Lecture(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=120)
    start_date =models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    lecture_created = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name="course", null=True, blank=True)
    classroom = models.CharField(choices=CLASSROOMS, max_length=100)
    lecturer = models.ForeignKey(Teacher, on_delete=models.PROTECT, related_name="lecture", null=True, blank=True)
    qr = models.ImageField(
		upload_to=image_path,
        null=True,
        blank=True
	)

    def __str__(self):
        return self.title

    def generate_qr(self):
        attendace_path = reverse("mark-attendance", args=[self.slug])
        attendace_url = urljoin(settings.BASE_URL, attendace_path)

        qrc = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
    
        qrc.add_data(attendace_url)
        qrc.make(fit=True)

        qr_image = qrc.make_image(fill_color="black", back_color="white")

        return qr_image

    def save(self, *args, **kwargs) -> None:
        
        if not self.slug:
            self.slug = slugify(self.title)

        if not self.qr:
            qr_image = self.generate_qr()
            image_stream = BytesIO()
            qr_image.save(image_stream, format='PNG')
            image_stream.seek(0)
            image_content = ContentFile(image_stream.read())
            self.qr.save('qr_code.png', image_content, save=False)

        super().save(*args, **kwargs)
