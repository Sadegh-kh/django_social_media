from django.contrib import admin

from . import models


class ImageInline(admin.TabularInline):
    extra = 1
    model = models.Image


class CommentInline(admin.TabularInline):
    extra = 0
    model = models.Comment


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["author", "created"]
    list_filter = ["created"]
    ordering = ["-created"]
    raw_id_fields = ["author"]
    search_fields = ["author", "description"]
    inlines = [ImageInline, CommentInline]


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "username", "created"]
    ordering = ["-created"]
    search_fields = ["username", "post"]
    list_filter = ["created", "updated"]


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["post", "created"]
