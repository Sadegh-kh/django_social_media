from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UsernameField,
)


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "phone"]

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if get_user_model().objects.filter(phone=phone).exists():
            raise forms.ValidationError("This phone number exist!")
        if len(phone) < 11:
            raise forms.ValidationError("leangh of phone number must be 11")
        if not phone.isnumeric():
            raise forms.ValidationError("phone number must be numeric")
        return phone


class LoginForm(AuthenticationForm):
    username = UsernameField(label="Username or Phone")


class EditUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "job",
            "age",
            "bio",
            "birth_date",
            "photo",
        ]

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if (
            get_user_model()
            .objects.exclude(id=self.instance.id)
            .filter(phone=phone)
            .exists()
        ):
            raise forms.ValidationError("This phone number exist!")
        return phone
