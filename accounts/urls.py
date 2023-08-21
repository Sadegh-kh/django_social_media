from django.contrib.auth.views import LoginView
from django.urls import path

from . import forms, views

app_name = "accounts"
urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(form_class=forms.LoginForm), name="login"),
]
