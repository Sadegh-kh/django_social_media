from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ["username", "phone", "first_name", "last_name", "email", "is_staff"]
    ordering = ["-is_staff", "username"]

    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Information",
            {
                "fields": ("photo", "job", "phone", "age", "birth_date", "bio"),
            },
        ),
    )  # type: ignore

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional Information",
            {
                "fields": ("photo", "job", "phone", "age", "birth_date", "bio"),
            },
        ),
    )
