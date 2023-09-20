from django.urls import path

from . import views

app_name = "social"
urlpatterns = [
    path("posts/", views.post_list, name="post_list"),
    path("ticket/", views.ticket, name="ticket"),
]
