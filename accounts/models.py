# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
def user_dirctory_path(instance, filename):
    return f"avatar/{instance.username}/{filename}"


class User(AbstractUser):
    phone = models.CharField(max_length=11, null=True, blank=True)
    job = models.CharField(max_length=100, null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to=user_dirctory_path, null=True, blank=True)

    followers = models.ManyToManyField(
        "self",
        through="Contact",
        related_name="following",
        symmetrical=False,
    )


class Contact(models.Model):
    user_from = models.ForeignKey(
        User, related_name="rel_from_set", on_delete=models.CASCADE
    )
    user_to = models.ForeignKey(
        User, related_name="rel_to_set", on_delete=models.CASCADE
    )
    follow_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-follow_at"]
        indexes = [
            models.Index(fields=["-follow_at"]),
        ]
