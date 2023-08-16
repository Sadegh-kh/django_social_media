from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ["username", "phone", "first_name", "last_name", "email", "is_staff"]
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Information",
            {
                "fields": ("photo", "job", "age", "birth_date", "bio"),
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional Information",
            {
                "fields": ("photo", "job", "age", "birth_date", "bio"),
            },
        ),
    )
