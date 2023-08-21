from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UsernameField,
)


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email"]


class LoginForm(AuthenticationForm):
    username = UsernameField(label="Username or Phone")
