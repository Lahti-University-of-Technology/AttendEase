from django.contrib import admin

from apps.users.models import User, Teacher, Student

# Register your models here.
admin.site.register([User, Teacher, Student])
