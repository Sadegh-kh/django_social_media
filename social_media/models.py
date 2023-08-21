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
