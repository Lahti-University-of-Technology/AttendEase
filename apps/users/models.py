from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class User(AbstractUser):
    # adding custom field
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'  # now user can log in using email
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']  # here, email is already a required field

    def __str__(self):
        return self.username
    
    @property
    def is_student(self):
        return hasattr(self, 'student')
    
    @property
    def is_teacher(self):
        return hasattr(self, 'teacher')


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student")

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher")

    def __str__(self):
        return self.user.username