from django.urls import path

from . import views

app_name = "social"
urlpatterns = [
    path("ticket/", views.ticket, name="ticket"),
]
