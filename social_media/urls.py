from django.urls import path

from . import views

app_name = "social"
urlpatterns = [
    path("posts/", views.post_list, name="post_list"),
    path("posts/<slug:slug_tag>", views.post_list, name="post_list_by_tag"),
    path("posts/post/create", views.create_post, name="post_create"),
    path("ticket/", views.ticket, name="ticket"),
]
