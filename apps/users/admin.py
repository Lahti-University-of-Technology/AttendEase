from django.contrib import admin
from apps.users.models import Teacher, Student
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

USER = get_user_model()

class CustomUserAdmin(UserAdmin):
    # at the time of user creation we want 'email', 'username', and 'password' fields so
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

admin.site.register(USER, CustomUserAdmin)
admin.site.register([Teacher, Student])