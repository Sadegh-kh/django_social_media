from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django_resized import ResizedImageField
from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    # relation
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="user_posted",
    )
    # data fields
    description = models.TextField()

    # date fields
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ["-created"]
        indexes = [models.Index(fields=["-created"])]

    def __str__(self):
        return self.author.username

    def get_absolute_url(self):
        return reverse("soctial:post_item", args=[self.id])

    def delete(self, *args, **kwargs):
        images = self.images.all()
        for image in images:
            # storage is django backend storage (media/) and path is exact location of file
            storage, path = image.image_file.storage, image.image_file.path
            storage.delete(path)
        super().delete(*args, **kwargs)


class Comment(models.Model):
    # post.comments/ post.comments.all() / comment.post
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    username = models.CharField(
        max_length=255,
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created"]
        indexes = [models.Index(fields=["-created"])]

    def __str__(self):
        return f"{self.username} : {self.post}"


def upload_to(instance, filename):
    datetime = timezone.now()
    return f"post_images/{datetime.strftime('%Y')}/{datetime.strftime('%m')}/{instance.post.auther.username}/{filename}"


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image_file = ResizedImageField(upload_to=upload_to, size=[300, 300], quality=75)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        indexes = [models.Index(fields=["-created"])]

    def __str__(self):
        image_name = self.image_file.name.split("/")[-1]
        return self.post if self.post else image_name

    def delete(self, *args, **kwargs):
        image = self.image_file
        storage, path = image.storage, image.path
        storage.delete(path)
        super().delete(*args, **kwargs)
