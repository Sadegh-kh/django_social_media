from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from . import forms

# Create your tests here.


class UserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username="test_user",
            password="Test3223131",
            email="test@gmail.com",
            phone="09123352345",
        )
        cls.signup_form = forms.SignUpForm
        cls.signup_data_form = {
            "username": "new_user",
            "email": "newtest@gmail.com",
            "phone": "09123456873",
            "password1": "Test3223131",
            "password2": "Test3223131",
        }

    def test_user_obj(self):
        self.assertEquals(self.user.username, "test_user")
        self.assertEquals(self.user.password, "Test3223131")
        self.assertEquals(self.user.email, "test@gmail.com")
        self.assertEquals(self.user.phone, "09123352345")

    def test_signup_correct_location(self):
        response = self.client.get(reverse("accounts:signup"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup(self):
        response = self.client.post(
            reverse("accounts:signup"),
            {
                "username": "new_user",
                "email": "newtest@gmail.com",
                "phone": "09123456873",
                "password1": "Test3223131",
                "password2": "Test3223131",
            },
        )
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse("accounts:login"))

    def test_signup_form(self):
        form = self.signup_form(self.signup_data_form)
        self.assertTrue(form.is_valid())

    def test_invalid_phone_signup_form(self):
        self.signup_data_form.update({"phone": "0912asd6873"})
        form = self.signup_form(data=self.signup_data_form)
        self.assertFalse(form.is_valid())
        self.assertIn("phone", form.errors.keys())
        self.assertIn("phone number must be numeric", form.errors["phone"])

    def test_phone_number_exist_signup_form(self):
        self.signup_data_form.update({"phone": "09123352345"})
        form = self.signup_form(data=self.signup_data_form)
        self.assertFalse(form.is_valid())
        self.assertIn("phone", form.errors.keys())
        self.assertIn("This phone number exist!", form.errors["phone"])
