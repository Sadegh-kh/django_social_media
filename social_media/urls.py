from django.urls import path

from . import views

app_name = "social"
urlpatterns = [
    path("posts/", views.post_list, name="post_list"),
    path("posts/<slug:slug_tag>", views.post_list, name="post_list_by_tag"),
    path("posts/create/post", views.create_post, name="post_create"),
    path("posts/post/<int:pk>", views.post_detail, name="post_detail"),
    path("ticket/", views.ticket, name="ticket"),
]
